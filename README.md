# scruby-plugin

Library for creating plugins for <a href="https://pypi.org/project/scruby/" alt="Scruby">Scruby</a>.

<br>
<br>

<p>
    <a href="https://github.com/kebasyaty/scruby-plugin/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/scruby-plugin/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
    <a href="https://pypi.python.org/pypi/scruby-plugin/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/scruby-plugin.svg" alt="PyPI pyversions"></a>
    <a href="https://pypi.python.org/pypi/scruby-plugin/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/scruby-plugin.svg" alt="PyPI status"></a>
    <a href="https://pypi.python.org/pypi/scruby-plugin/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/scruby-plugin.svg" alt="PyPI version fury.io"></a>
    <br>
    <a href="https://pyrefly.org/" alt="Types: Pyrefly"><img src="https://img.shields.io/badge/types-Pyrefly-FFB74D.svg" alt="Types: Pyrefly"></a>
    <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
    <a href="https://pypi.org/project/scruby-plugin"><img src="https://img.shields.io/pypi/format/scruby-plugin" alt="Format"></a>
    <a href="https://pepy.tech/projects/scruby-plugin"><img src="https://static.pepy.tech/badge/scruby-plugin" alt="PyPI Downloads"></a>
    <a href="https://github.com/kebasyaty/scruby-plugin/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/scruby-plugin" alt="GitHub license"></a>
</p>

<br>

[![Requirements](https://raw.githubusercontent.com/kebasyaty/scruby-plugin/v0/assets/links/requirements.svg "Requirements")](https://github.com/kebasyaty/scruby-plugin/blob/v0/REQUIREMENTS.md "Requirements")

## Installation

```shell
uv add scruby-plugin
```

## Usage

```python
from typing import Any
from scruby_plugin import ScrubyPlugin

class PluginName(ScrubyPlugin):
    def __init__(self, scruby_self: Any) -> None:
        ScrubyPlugin.__init__(self, scruby_self)

    ...your code...
```

## Example

```python
import anyio
from typing import Any
from pydantic import Field
from scruby import Scruby, ScrubyModel, ScrubySettings
from scruby_plugin import ScrubyPlugin
from pprint import pprint as pp


# Create plugin
class CollectionMeta(ScrubyPlugin):
    def __init__(self, scruby_self: Any) -> None:
        ScrubyPlugin.__init__(self, scruby_self)

    async def get(self) -> Any:
        scruby_self = self.scruby_self()
        return await scruby_self.get_meta()


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


async def main() -> None:
    # Get collection `Car`.
    car_coll = await Scruby.collection(Car)
    # Get metadata of collection
    meta = await car_coll.plugins.collectionMeta.get()
    # Print to console
    pp(meta)
    #
    # Full database deletion.
    # Hint: The main purpose is tests.
    Scruby.napalm()

if __name__ == "__main__":
    anyio.run(main)
```

<br>

[![Changelog](https://raw.githubusercontent.com/kebasyaty/scruby-plugin/v0/assets/links/changelog.svg "Changelog")](https://github.com/kebasyaty/scruby-plugin/blob/v0/CHANGELOG.md "Changelog")

[![MIT](https://raw.githubusercontent.com/kebasyaty/scruby-plugin/v0/assets/links/mit.svg "MIT")](https://github.com/kebasyaty/scruby-plugin/blob/main/LICENSE "MIT")
