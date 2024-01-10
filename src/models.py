from importlib import import_module
from setting import APPS

for app in APPS:
    models_module = f"{app}.models"
    try:
        import_module(models_module)

    except ModuleNotFoundError:
        print(f"App Model for models not found: {app}")

