import unittest

from algorithm_services.config import config
from algorithm_services.app import create_app

from flask import Flask


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(__name__, config)

    def test_create_app(self):
        self.assertTrue(isinstance(self.app, Flask))

    def test_create_app_config(self):
        self.assertEqual(
            self.app.config['DEBUG'],
            True
        )
        self.assertEqual(
            self.app.config['TEMPLATES_AUTO_RELOAD'],
            True
        )
        self.assertEqual(
            self.app.config['EXPLAIN_TEMPLATE_LOADING'],
            True
        )

    def test_crete_app_routes(self):
        self.assertEquals(
            5,
            len(list(self.app.url_map.iter_rules()))
        )
