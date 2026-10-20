import pytest

from product import Product
from category import Category


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


def test_category_products_property_print(first_product, second_category):
    print(second_category.products)


def test_category_products_property(first_product, second_category):
    assert second_category.products == (
        f"{first_product.name}, {first_product.price} руб. "
        f"Остаток: {first_product.quantity} шт.\n"
    )


def test_product_price_setter(first_product):
    """Тестируем режим доступа (геттер и сеттер) для цены продукта"""
    # 1. Проверяем успешное изменение через сеттер
    first_product.price = 50000.0
    assert first_product.price == 50000.0

    # 2. Проверяем защиту сеттера от некорректных данных (цена <= 0)
    first_product.price = -100
    assert first_product.price == 50000.0  # Цена не должна была измениться


def test_category_add_product(first_product, second_category):
    """Тестируем режим доступа к продуктам категории через метод add_product"""
    # Считаем, сколько товаров в строке изначально (из фикстуры там 1 товар)
    # Наш геттер возвращает строку, проверяем, что в ней есть имя первого продукта
    assert first_product.name in second_category.products

    # Создаем еще один продукт для проверки добавления
    new_prod = Product("Xiaomi", "Budget phone", 20000.0, 5)

    # Добавляем продукт в категорию через публичный метод
    second_category.add_product(new_prod)

    # Проверяем через геттер, что новый продукт успешно добавился в скрытый список
    assert "Xiaomi" in second_category.products
