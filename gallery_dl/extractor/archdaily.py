# -*- coding: utf-8 -*-

# Copyright 2021 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

# TODO: Ckeck documentation / discussion on extractor creation
# https://github.com/mikf/gallery-dl/discussions/1656

"""Extractors for https://architizer.com/"""

from .common import GalleryExtractor, Extractor, Message
from .. import text



    def __init__(self, match):
        pattern = r"(?:https?://)?archdaily\.com/\d{10}/([^/?#]+)"
        url = "{}/projects/{}/".format(self.root, match.group(1))
        GalleryExtractor.__init__(self, match, url)
