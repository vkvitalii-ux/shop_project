import pytest
from main import Product, Category


@pytest.fixture(autouse=True)
def clean_counters():
    """Фикстура автоматически сбрасывает счётчики классов перед тестом."""
    Category.category_count = 0
    Category.product_count = 0
    Category._unique_products = set()
    yield


def test_product_initialization():
    """Тест проверяет корректность создания объекта Product."""
    product = Product("Product", "Description", 30000.0, 3)

    assert product.name == "Product"
    assert product.description == "Description"
    assert product.price == 30000.0
    assert product.quantity == 3


def test_category_initialization_and_counts():
    """Тест проверяет создание категорий и подсчет уникальных продуктов."""
    prod1 = Product("Samsung S23", "256GB", 90000.0, 10)
    prod2 = Product("Iphone 15", "512GB", 210000.0, 5)
    prod3 = Product("Samsung S23", "Дубликат", 90000.0, 1)

    # Создаем первую категорию
    cat1 = Category("Смартфоны", "Гаджеты", [prod1, prod2, prod3])

    assert cat1.name == "Смартфоны"
    assert cat1.description == "Гаджеты"
    assert cat1.products == [prod1, prod2, prod3]

    assert Category.category_count == 1
    assert Category.product_count == 2

    # Создаем вторую категорию
    prod4 = Product("Xiaomi Note 11", "128GB", 310000.0, 2)
    cat2 = Category("Телефоны", "Другие", [prod4])

    # Проверяем cat2, чтобы убрать ошибку неиспользованной переменной
    assert cat2.name == "Телефоны"

    assert Category.category_count == 2
    assert Category.product_count == 3
