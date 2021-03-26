# -*- coding: utf-8 -*-
"""Top-level package for topalias."""

__author__ = "Sergey Chudakov"
__email__ = "csredrat@gmail.com"
__version__ = "2.0.20"

import json
import os
import sys

import requests

from packaging.version import parse as version_parse


sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__))),
)  # noqa: WPS221
# isort: split  # noqa: E800

# pylint: disable=wrong-import-position
# pylint: enable=wrong-import-position

TOPALIAS_PYPI_LATEST_VERSION = "https://pypi.python.org/pypi/topalias/json"


def get_version(url=TOPALIAS_PYPI_LATEST_VERSION):
    """Return version of topalias package on pypi.org."""
    req = requests.get(url)
    version = version_parse("0")
    if req.status_code == requests.codes.ok:  # pylint: disable=E1101
        req.encoding = req.apparent_encoding
        j = json.loads(req.text.encode(req.encoding))
        releases = j.get("releases", [])
        for release in releases:
            ver = version_parse(release)
            if not ver.is_prerelease:
                version = max(version, ver)
    return version
