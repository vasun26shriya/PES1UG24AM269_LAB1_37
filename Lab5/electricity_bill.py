"""Calculate slab-based electricity bills and persist the demo results."""

import http.client
import ipaddress
import json

from defusedxml import ElementTree

SLABS = [(100, 3.5), (200, 5.0), (300, 6.5)]
HIGH_RATE = 8.0
FIXED_CHARGE = 75
METER_XML = ("<meters>"
             "<meter id='M1' prev='1200' curr='1350'/>"
             "<meter id='M2' prev='5000' curr='5420'/>"
             "<meter id='M3' prev='800' curr='760'/>"
             "</meters>")
BILLS = []


def read_meters(xml_text):
    """Parse meter IDs and integer readings using a hardened XML parser."""
    root = ElementTree.fromstring(xml_text)
    return [(meter.get("id"), int(meter.get("prev")),
             int(meter.get("curr"))) for meter in root.findall("meter")]


def calculate_units(previous, current):
    """Return consumption, warning and returning zero for reversed readings."""
    if current < previous:
        print("Warning: meter reading went backwards")
        return 0
    return current - previous


def energy_charge(units):
    """Apply the progressive tariff slabs and the remaining high-rate band."""
    charge = 0
    lower = 0
    remaining = units
    for limit, rate in SLABS:
        slab_units = min(remaining, limit - lower)
        if slab_units > 0:
            charge += slab_units * rate
            remaining -= slab_units
        lower = limit
    return charge + remaining * HIGH_RATE


def generate_bill(meter_id, units, tax_rate=0.05, extras=None):
    """Create and record a bill with optional fees and tax."""
    if extras is None:
        extras = {}
    amount = energy_charge(units) + FIXED_CHARGE + sum(extras.values())
    bill = {"meter": meter_id, "units": units,
            "amount": round(amount * (1 + tax_rate), 2)}
    BILLS.append(bill)
    return bill


def average_bill():
    """Return the mean bill amount, or zero when no bills exist."""
    if not BILLS:
        return 0
    return round(sum(bill["amount"] for bill in BILLS) / len(BILLS), 2)


def save_bills(file_name="bills.json"):
    """Write recorded bills as UTF-8 JSON."""
    with open(file_name, "w", encoding="utf-8") as bill_file:
        json.dump(BILLS, bill_file, indent=2)


def sync_meter(meter_ip):
    """Fetch a reading over verified HTTPS from a validated IP address."""
    address = str(ipaddress.ip_address(meter_ip))
    connection = http.client.HTTPSConnection(address, timeout=10)
    try:
        connection.request("GET", "/reading")
        response = connection.getresponse()
        if response.status != 200:
            raise OSError(f"Meter returned HTTP status {response.status}")
        return response.read()
    finally:
        connection.close()


def main():
    """Run the billing demonstration without accumulating old bills."""
    BILLS.clear()
    for meter_id, previous, current in read_meters(METER_XML):
        units = calculate_units(previous, current)
        generate_bill(meter_id, units)
    generate_bill("M4", 50, extras={"late_fee": 25})
    for bill in BILLS:
        print(bill["meter"], "used", bill["units"], "units, bill Rs.",
              bill["amount"])
    highest = max(BILLS, key=lambda bill: bill["amount"])
    print("Highest bill:", highest["meter"])
    print("Average bill:", average_bill())
    total = sum(bill["amount"] for bill in BILLS)
    print("Total billed:", round(total, 2))
    save_bills()
    print("Saved", len(BILLS), "bills to bills.json")


if __name__ == "__main__":
    main()
