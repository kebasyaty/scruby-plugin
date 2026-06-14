"""Test ScrubyPlugin."""

from __future__ import annotations

from typing import Any

import pytest
from pydantic import Field
from scruby import Scruby, ScrubyModel

from scruby_plugin import ScrubyPlugin

pytestmark = pytest.mark.asyncio(loop_scope="module")


# Create plugin
class CollectionMeta(ScrubyPlugin):
    """Example."""

    def __init__(self, scruby_self: Scruby) -> None:  # noqa: D107
        ScrubyPlugin.__init__(self, scruby_self)

    async def get(self) -> Any:
        """Print metadata to console."""
        scruby_self = self.scruby_self()
        return await scruby_self.get_meta()


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


# Activate database.
Scruby.run(plugins=[CollectionMeta])


async def test_scruby_plugin() -> None:
    """Test ScrubyPlugin."""
    # Get collection `Car`.
    car_coll = await Scruby.collection(Car)
    meta = await car_coll.plugins.collectionMeta.get()

    match ScrubyPlugin.SCRUBY_VERSION:
        case 0:
            assert ScrubyPlugin.SCRUBY_VERSION == 0
            assert CollectionMeta.SCRUBY_VERSION == 0
            assert meta.collection_name == "Car"
            assert meta.hash_reduce_left == 6
            assert meta.max_number_branch == 256
            assert meta.counter_documents == 0
        case 1:
            assert ScrubyPlugin.SCRUBY_VERSION == 1
            assert CollectionMeta.SCRUBY_VERSION == 1
            assert meta.collection_name == "Car"
            assert meta.hash_reduce_left == 6
            assert meta.max_number_branch == 256
            assert meta.counter_documents == 0
        case 2:
            assert ScrubyPlugin.SCRUBY_VERSION == 2
            assert CollectionMeta.SCRUBY_VERSION == 2
            assert meta.collection_name == "Car"
            assert meta.hash_reduce_left == 7
            assert meta.max_number_branch == 16
            assert meta.counter_documents == 0
    #
    # Delete DB.
    Scruby.napalm()
