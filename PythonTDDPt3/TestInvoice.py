import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5}, 'Notebook': {'qnt': 5, 'unit_price': 7.5,
                                                                                   'discount': 10}}
    return products

@pytest.fixture()
def products2():
    products2 = {'Paper': {'qnt': 5, 'unit_price': 2, 'discount': 1}}
    return products2

@pytest.fixture()
def no_discount():
    no_discount = {'Paper': {'qnt': 10, 'unit_price': 3.75, 'discount': 0}}
    return no_discount

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75


def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62


def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38


def test_NoDiscount(invoice, no_discount):
    invoice.totalPurePrice(no_discount)
    assert invoice.totalPurePrice(no_discount) == 37.50


def test_whichProductCostMore(invoice, products, products2):
    invoice.whichProductCostMore(products, products2)
    assert invoice.whichProductCostMore(products, products2) == products