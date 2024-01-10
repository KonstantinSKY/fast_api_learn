from importlib import import_module
from fastapi import APIRouter
from setting import APPS

routers = APIRouter()
for app in APPS:
    app_router_module = f"{app}.router"
    try:
        router_module = import_module(app_router_module)
        if hasattr(router_module, 'router'):
            app_router = getattr(router_module, 'router')
            routers.include_router(app_router)
            # print(f"App Router included from App module: {app_router_module}")
        else:
            print(f"Router not found in App module {app_router_module}")

    except ModuleNotFoundError:
        print(f"App Router not found: {app_router_module}")

