from unittest import TestCase
from models.item import ItemModel


class TestItem(TestCase):
    def test__init__(self):
        item_model = ItemModel('Test', 80.00)
        self.assertEqual(item_model.name, 'Test')
        self.assertEqual(item_model.price, 80.00)

    def test_json(self):
        item_model = ItemModel('Test', 80.00)
        self.assertEqual(item_model.json(), {'name': 'Test', 'price': 80.00})

    def test_find_by_name(self):
        pass

    def test_save_to_db(self):
        pass

    def test_delete_from_db(self):
        pass
