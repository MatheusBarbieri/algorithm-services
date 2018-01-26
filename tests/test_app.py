import unittest

from algorithm_services.config import config
from algorithm_services.app import create_app

from flask import Flask


class AppTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, config)
        self.app = _app.test_client()
        self.app.testing = True

    def test_create_app(self):
        self.assertTrue(isinstance(self.app.application, Flask))

    def test_create_app_config(self):
        self.assertEqual(
            self.app.application.config['DEBUG'],
            True
        )
        self.assertEqual(
            self.app.application.config['TEMPLATES_AUTO_RELOAD'],
            True
        )
        self.assertEqual(
            self.app.application.config['EXPLAIN_TEMPLATE_LOADING'],
            True
        )

    def test_crete_app_routes(self):
        self.assertLess(
            2,
            len(list(self.app.application.url_map.iter_rules()))
        )
