"""Lab 6 line coverage - Shriya Vasundhara Singh, PES1UG24AM269."""
import pytest
from vending_machine import select_item, make_change, purchase


@pytest.mark.parametrize('item,stock,credit,expected', [
    ('water', {}, 100, 'invalid'),
    ('cola', {}, 150, 'sold_out'),
    ('cola', {'cola': 1}, 149, 'insufficient'),
    ('cola', {'cola': 1}, 150, 'ok'),
])
def test_selection(item, stock, credit, expected):
    before = stock.copy()
    assert select_item(item, stock, credit) == expected
    assert stock == before


def test_negative_change():
    with pytest.raises(ValueError, match='negative amount'):
        make_change(-1)


@pytest.mark.parametrize('amount,expected', [
    (0, []), (290, [100, 100, 50, 25, 10, 5]), (1, None),
])
def test_change(amount, expected):
    assert make_change(amount) == expected


def test_rejected_purchase():
    stock = {'cola': 1}
    assert purchase('water', stock, 200) == ('invalid', [])
    assert stock == {'cola': 1}


def test_unrepresentable_change():
    stock = {'cola': 1}
    assert purchase('cola', stock, 151) == ('no_exact_change', [])
    assert stock == {'cola': 1}


def test_successful_purchase():
    stock = {'cola': 2, 'chips': 3}
    assert purchase('cola', stock, 200) == ('dispensed', [50])
    assert stock == {'cola': 1, 'chips': 3}
