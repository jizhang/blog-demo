import logging
import pkgutil
import importlib

logger = logging.getLogger(__name__)


def import_submodules(package: str):
    mod = importlib.import_module(package)
    for _, name, is_pkg in pkgutil.iter_modules(mod.__path__):
        full_name = mod.__name__ + '.' + name
        if is_pkg:
            import_submodules(full_name)
        else:
            importlib.import_module(full_name)
