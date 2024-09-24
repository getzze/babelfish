# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import annotations

from babelfish.language import LANGUAGE_MATRIX

from . import LanguageEquivalenceConverter


class Alpha2Converter(LanguageEquivalenceConverter):
    CASE_SENSITIVE = True
    SYMBOLS = {}
    for iso_language in LANGUAGE_MATRIX:
        if iso_language.alpha2:
            SYMBOLS[iso_language.alpha3] = iso_language.alpha2
