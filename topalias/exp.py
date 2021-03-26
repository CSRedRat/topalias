# -*- coding: utf-8 -*-
"""Other experimental functions."""

import json

import requests

from packaging.version import parse as version_parse


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


print(
    f"Latest release: {get_version()} on https://pypi.org/project/topalias/\n",
)
