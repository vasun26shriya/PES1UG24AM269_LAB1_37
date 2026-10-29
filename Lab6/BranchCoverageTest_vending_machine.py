"""Lab 6 branch coverage - Shriya Vasundhara Singh, PES1UG24AM269."""
import pytest
from vending_machine import PRICES, select_item, make_change, purchase


@pytest.mark.parametrize('item', list(PRICES))
def test_price_boundary(item):
    stock = {item: 1}
    assert select_item(item, stock, PRICES[item] - 1) == 'insufficient'
    assert select_item(item, stock, PRICES[item]) == 'ok'
    assert select_item(item, stock, PRICES[item] + 1) == 'ok'
    assert stock == {item: 1}


@pytest.mark.parametrize('item,stock,credit,status', [
    ('water', {}, 200, 'invalid'),
    ('cola', {}, 200, 'sold_out'),
    ('chips', {'chips': 0}, 200, 'sold_out'),
    ('candy', {'candy': 1}, 74, 'insufficient'),
])
def test_rejection_preserves_stock(item, stock, credit, status):
    before = stock.copy()
    assert purchase(item, stock, credit) == (status, [])
    assert stock == before


@pytest.mark.parametrize('amount,expected', [
    (0, []), (5, [5]), (10, [10]), (25, [25]), (50, [50]),
    (100, [100]), (290, [100, 100, 50, 25, 10, 5]),
    (1, None), (4, None), (6, None), (101, None),
])
def test_change_branches(amount, expected):
    assert make_change(amount) == expected


def test_negative_change():
    with pytest.raises(ValueError, match='^negative amount$'):
        make_change(-1)


@pytest.mark.parametrize('item', list(PRICES))
@pytest.mark.parametrize('extra,change', [(0, []), (50, [50]), (290, [100, 100, 50, 25, 10, 5])])
def test_dispense_and_stock(item, extra, change):
    stock = {'cola': 2, 'chips': 2, 'candy': 2}
    before = stock.copy()
    assert purchase(item, stock, PRICES[item] + extra) == ('dispensed', change)
    before[item] -= 1
    assert stock == before


def test_no_exact_change_preserves_stock():
    stock = {'cola': 1}
    assert purchase('cola', stock, 151) == ('no_exact_change', [])
    assert stock == {'cola': 1}


def test_last_item_then_sold_out():
    stock = {'candy': 1}
    assert purchase('candy', stock, 75) == ('dispensed', [])
    assert purchase('candy', stock, 75) == ('sold_out', [])
    assert stock == {'candy': 0}
