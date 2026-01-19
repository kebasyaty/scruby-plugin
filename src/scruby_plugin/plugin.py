# Scruby-Plugin - Library for creating Scruby plugins.
# Copyright (c) 2026 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Contains the base class for creating Scruby plugins."""

from __future__ import annotations

__all__ = ("ScrubyPlugin",)

import weakref
from typing import Any


class ScrubyPlugin:
    """Base class for creating Scruby plugins."""

    def __init__(self, scruby: Any) -> None:  # noqa: D107
        self.scruby = weakref.ref(scruby)
