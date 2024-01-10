from importlib import import_module
from fastapi import APIRouter
from setting import APPS

api_router = APIRouter()
for app in APPS:
    try:
        router_module = import_module(app)
        router = getattr(router_module, 'router', None)
        if router:
            api_router.include_router(router.router)
        else:
            print(f"Router not found in App module {router}")

    except ModuleNotFoundError:
        print(f"App Model for Router not found: {app}")

