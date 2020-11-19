# -*- coding: utf-8 -*-
"""Tests for `topalias` package."""

import pytest
import requests
from bs4 import BeautifulSoup
from click.testing import CliRunner
from topalias import aliascore, cli


@pytest.fixture(name="response")
def fixture_response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    return requests.get("https://github.com/CSRedRat/topalias")


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""

    assert "GitHub" in BeautifulSoup(response.content, features="html5lib").title.string


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        ("test", "console util test\n"),
    ],
)
def test_welcome(capsys, message: str, expected: str):
    """Test output to stdout"""
    aliascore.welcome(message)
    out, err = capsys.readouterr()
    assert out == expected, err == ""


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    history_output = runner.invoke(cli.cli, ["history"])
    assert history_output.exit_code == 0
    assert "Run after add alias: " in history_output.output
    help_result = runner.invoke(cli.cli, ["--debug", "--help"])
    assert help_result.exit_code == 0
    assert "-h, --help            Show this message and exit." in help_result.output