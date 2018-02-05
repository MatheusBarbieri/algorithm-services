import unittest

from algorithm_services.app import create_app

from flask import Flask


class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Configuration test data
        self.config = {
            "DEBUG": True,
            "TEMPLATES_AUTO_RELOAD": True,
            "EXPLAIN_TEMPLATE_LOADING": True,
            "TEMPLATE_FOLDER": "./algorithm_services/templates"
        }

        self.app = create_app(__name__, self.config)

    def test_create_app(self):
        self.assertTrue(isinstance(self.app, Flask))

    def test_create_app_config(self):
        self.assertEqual(
            self.app.config['DEBUG'],
            self.config['DEBUG']
        )
        self.assertEqual(
            self.app.config['TEMPLATES_AUTO_RELOAD'],
            self.config['TEMPLATES_AUTO_RELOAD']
        )
        self.assertEqual(
            self.app.config['EXPLAIN_TEMPLATE_LOADING'],
            self.config['EXPLAIN_TEMPLATE_LOADING']
        )

    def test_crete_app_routes(self):
        self.assertEquals(
            3,
            len(list(self.app.url_map.iter_rules()))
        )
