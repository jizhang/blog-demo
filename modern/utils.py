import logging
import pkgutil
import importlib
from types import ModuleType

logger = logging.getLogger(__name__)


def import_submodules(module: ModuleType):
    for _, name, is_pkg in pkgutil.iter_modules(module.__path__):
        full_name = f'{module.__name__}.{name}'
        logger.debug(f'Import module: {full_name}')
        submodule = importlib.import_module(full_name)
        if is_pkg:
            import_submodules(submodule)
