import inspect
from abc import abstractproperty
from functools import lru_cache
from types import ModuleType
from typing import Any
from typing import cast
from typing import Dict
from typing import Generator
from typing import Type
from typing import TypeVar

from ... import plugins
from ...plugins.base import BasePlugin
from ...settings import get_settings
from ...util.importlib import import_file_as_module
from ...util.importlib import import_types_from_module
from ...util.importlib import import_types_from_package


Plugin = TypeVar('Plugin', bound=BasePlugin)


@lru_cache(maxsize=1)
def get_mapping_from_secret_type_to_class() -> Dict[str, Type[Plugin]]:
    output = {}
    for plugin_class in import_types_from_package(
        plugins,
        filter=lambda x: not _is_valid_plugin(x),
    ):
        output[plugin_class.secret_type] = plugin_class

    # Load custom plugins.
    # NOTE: It's entirely possible that once the baseline is created, it is modified by
    # someone to cause this to break (e.g. arbitrary imports from unexpected places).
    # However, this falls under the same security assumptions as listed in
    # `import_file_as_module`.
    for classname, config in get_settings().plugins.items():
        if 'path' not in config:
            continue

        # Only supporting file schema right now.
        filename = config['path'][len('file://'):]
        for plugin_class in get_plugins_from_file(filename):
            output[cast(BasePlugin, plugin_class).secret_type] = plugin_class

    return output


def get_plugins_from_file(filename: str) -> Generator[Type[Plugin], None, None]:
    plugin_class: Type[Plugin]
    for plugin_class in get_plugins_from_module(import_file_as_module(filename)):
        yield plugin_class


def get_plugins_from_module(module: ModuleType) -> Generator[Type[Plugin], None, None]:
    for plugin_class in import_types_from_module(module, filter=lambda x: not _is_valid_plugin(x)):
        yield cast(Type[Plugin], plugin_class)


def _is_valid_plugin(attribute: Any) -> bool:
    return (
        inspect.isclass(attribute)
        and issubclass(attribute, BasePlugin)
        # Heuristic to determine abstract classes
        and not isinstance(attribute.secret_type, abstractproperty)
    )
