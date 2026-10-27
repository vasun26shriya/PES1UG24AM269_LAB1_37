"""Behavior and security regression checks for the fixed billing program."""
import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch, MagicMock

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    'electricity_bill', ROOT / 'electricity_bill.py')
MODULE = importlib.util.module_from_spec(SPEC)
IMPORT_OUTPUT = io.StringIO()
with contextlib.redirect_stdout(IMPORT_OUTPUT):
    SPEC.loader.exec_module(MODULE)


class BillingChecks(unittest.TestCase):
    def setUp(self):
        MODULE.BILLS.clear()

    def test_import_has_no_demo_output(self):
        self.assertEqual(IMPORT_OUTPUT.getvalue(), '')

    def test_slab_boundaries(self):
        for units, expected in [(0, 0), (50, 175), (100, 350),
                                (150, 600), (200, 850), (300, 1500),
                                (301, 1508), (420, 2460)]:
            with self.subTest(units=units):
                self.assertEqual(MODULE.energy_charge(units), expected)

    def test_reversed_reading(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(MODULE.calculate_units(800, 760), 0)

    def test_tax_and_extras(self):
        self.assertEqual(MODULE.generate_bill('M4', 50, extras={'late_fee': 25}),
                         {'meter': 'M4', 'units': 50, 'amount': 288.75})

    def test_empty_average_and_default_fees(self):
        self.assertEqual(MODULE.average_bill(), 0)
        self.assertEqual(MODULE.generate_bill('A', 0)['amount'], 78.75)
        self.assertEqual(MODULE.generate_bill('B', 0)['amount'], 78.75)

    def test_json_persistence(self):
        MODULE.generate_bill('A', 50)
        with tempfile.TemporaryDirectory(dir=ROOT) as folder:
            path = pathlib.Path(folder) / 'bills.json'
            MODULE.save_bills(path)
            self.assertEqual(json.loads(path.read_text()), MODULE.BILLS)

    def test_entity_payload_rejected(self):
        from defusedxml.common import DefusedXmlException
        with self.assertRaises(DefusedXmlException):
            MODULE.read_meters('<!DOCTYPE x [<!ENTITY x "123">]>'
                               '<meters>&x;</meters>')

    def test_command_injection_address_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.sync_meter('127.0.0.1; echo injected')

    def test_sync_uses_https_and_closes(self):
        connection = MagicMock()
        connection.getresponse.return_value.status = 200
        connection.getresponse.return_value.read.return_value = b'150'
        with patch.object(MODULE.http.client, 'HTTPSConnection',
                          return_value=connection) as constructor:
            self.assertEqual(MODULE.sync_meter('127.0.0.1'), b'150')
        constructor.assert_called_once_with('127.0.0.1', timeout=10)
        connection.request.assert_called_once_with('GET', '/reading')
        connection.close.assert_called_once()

    def test_sync_http_error_closes(self):
        connection = MagicMock()
        connection.getresponse.return_value.status = 503
        with patch.object(MODULE.http.client, 'HTTPSConnection',
                          return_value=connection):
            with self.assertRaises(OSError):
                MODULE.sync_meter('127.0.0.1')
        connection.close.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)
