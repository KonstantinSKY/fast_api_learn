from typing import AsyncGenerator
from importlib import import_module
from setting import APPS
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


metadata = Base.metadata

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


def alembic_config_set_sections(config):
    section = config.config_ini_section
    config.set_section_option(section, "DB_HOST", DB_HOST)
    config.set_section_option(section, "DB_PORT", DB_PORT)
    config.set_section_option(section, "DB_USER", DB_USER)
    config.set_section_option(section, "DB_NAME", DB_NAME)
    config.set_section_option(section, "DB_PASS", DB_PASS)


def import_app_models():
    for app in APPS:
        models_module = f"{app}.models"
        try:
            import_module(models_module)

        except ModuleNotFoundError:
            print(f"App Model for models not found: {app}")
