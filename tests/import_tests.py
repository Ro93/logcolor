"""
Import Tests
============
Make sure imports work as expected
"""
# Standard
from unittest import TestCase


class TestImports(TestCase):

    def test_import_color_stripper(self):
        """Test importing ColorStripper"""
        try:
            from logcolor import ColorStripper  # noqa
        except ImportError:
            raise AssertionError("Unable to import ColorStripper from module")

    def test_import_color_formatter(self):
        """Test importing ColorFormatter"""
        try:
            from logcolor import ColorFormatter  # noqa
        except ImportError:
            raise AssertionError("Unable to import ColorFormatter from module")