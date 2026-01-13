"""Test ScrubyPlugin."""

from __future__ import annotations

import logging
from typing import Any

import pytest
from pydantic import Field
from scruby import Scruby, ScrubyModel, settings

from scruby_plugin import ScrubyPlugin

pytestmark = pytest.mark.asyncio(loop_scope="module")


# Create plugin
class PrintMeta(ScrubyPlugin):
    """Example of ScrubyPlugin."""

    def __init__(self, scruby: Any) -> None:  # noqa: D107
        ScrubyPlugin.__init__(self, scruby)

    async def run(self) -> None:
        """Print metadata to console."""
        scruby = self.scruby()
        meta = await scruby.get_meta()
        logging.info(meta)


# Add plugin
settings.PLUGINS = [
    PrintMeta,
]


class Car(ScrubyModel):
    """Car model."""

    brand: str = Field(strict=True, frozen=True)
    model: str = Field(strict=True, frozen=True)
    year: int = Field(strict=True)
    power_reserve: int = Field(strict=True)
    # key is always at bottom
    key: str = Field(
        strict=True,
        frozen=True,
        default_factory=lambda data: f"{data['brand']}:{data['model']}",
    )


async def test_scruby_plugin() -> None:
    """Test ScrubyPlugin."""
    # Get collection `Car`.
    car_coll = await Scruby.collection(Car)
    await car_coll.plugins.printMeta.run()
    # Delete DB.
    Scruby.napalm()
