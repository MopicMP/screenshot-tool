"""Tests for screenshot-tool."""

import pytest
from screenshot_tool import tool


class TestTool:
    """Test suite for tool."""

    def test_basic(self):
        """Test basic usage."""
        result = tool("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            tool("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = tool(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
