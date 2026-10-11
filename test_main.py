import pytest

from main import Product, Category


@pytest.fixture
def first_product():
    return Product(
        name="Product",
        description="Product",
        price=30000,
        quantity=3
    )


@pytest.fixture
def category(first_product):
    return Category(
        name="Category",
        description="Category",
        products=[first_product]
    )


@pytest.fixture
def second_category(first_product):
    return Category(
        name="Category",
        description="Category",
        products=[first_product]
    )


def test_product_init(first_product):
    assert first_product.name == "Product"