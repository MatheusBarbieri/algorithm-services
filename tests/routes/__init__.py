class RouteTestCase(unittest.TestCase):

    def setUp(self):
        _app = create_app(__name__, {})
        self.app = _app.test_client()
        
