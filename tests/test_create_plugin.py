"""Test ScrubyPlugin."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import Field
from scruby import Scruby, ScrubyModel, ScrubySettings

from scruby_plugin import ScrubyPlugin

pytestmark = pytest.mark.asyncio(loop_scope="module")


# Create plugin
class CollectionMeta(ScrubyPlugin):
    """Example."""

    def __init__(self, scruby: Any) -> None:  # noqa: D107
        ScrubyPlugin.__init__(self, scruby)

    async def get(self) -> Any:
        """Print metadata to console."""
        scruby = self.scruby()
        return await scruby.get_meta()


# Plugins connection.
ScrubySettings.plugins = [
    CollectionMeta,
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
    meta = await car_coll.plugins.collectionMeta.get()
    assert meta.db_root == "ScrubyDB"
    assert meta.collection_name == "Car"
    assert meta.hash_reduce_left == 6
    assert meta.max_branch_number == 256
    assert meta.counter_documents == 0
    #
    # Delete DB.
    Scruby.napalm()
