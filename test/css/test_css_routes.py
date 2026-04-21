import unittest

from app import create_app


class CssBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("config.Test")
        self.client = self.app.test_client()
        self.domain = "http://localhost"

    def test_css(self):
        rv = self.client.get("/enrichment/css/logo-adornments.css")
        self.assertEqual(rv.status_code, 200)
