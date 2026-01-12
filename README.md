# scruby-plugin

Library for creating Scruby plugins.

## Requirements

[View the list of requirements](https://github.com/kebasyaty/scruby-plugin/blob/v0/REQUIREMENTS.md "Requirements").

## Installation

```shell
uv add scruby-plugin
```

## Usage

```python
from typing import Any
from scruby_plugin import ScrubyPlugin

class PluginName(ScrubyPlugin):
    def __init__(self, scruby: Any) -> None:
        ScrubyPlugin.__init__(self, scruby)

    ...your code...
```

## Changelog

[View the change history](https://github.com/kebasyaty/scruby-plugin/blob/v0/CHANGELOG.md "Changelog").

## License

This project is licensed under the [MIT](https://github.com/kebasyaty/scruby-plugin/blob/main/LICENSE "MIT").
