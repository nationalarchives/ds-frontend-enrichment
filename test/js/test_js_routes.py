import unittest

from app import create_app


class JavascriptBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Test").test_client()
        self.domain = "http://localhost"

    def test_javascript(self):
        rv = self.app.get("/enrichment/js/logo-adornments.js")
        self.assertEqual(rv.status_code, 200)
