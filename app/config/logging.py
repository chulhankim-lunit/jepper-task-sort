import os
import logging.config
import sys
from typing import Any

import tomlkit


def get_app_version() -> str:
    with open(file="pyproject.toml") as f:
        pyproject_toml = tomlkit.parse(string=f.read())
        return pyproject_toml["tool"]["poetry"]["version"]


def log(message: str, data: dict[str, Any]) -> str:
    return f"{message}: {' '.join([f'{k}={v}' for k, v in data.items()])}" if len(data) > 0 else f"{message}."


dt = "[%(asctime)s.%(msecs)03d]" if os.getenv("AWS_ENV", "local") == "local" else ""
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": True,
        "loggers": {
            "app.root": {"level": "INFO", "handlers": ["console"]},
        },
        "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "message", "stream": sys.stdout}},
        "formatters": {
            "message": {
                "format": f"{dt}[%(levelname)5.5s][{get_app_version()}][%(threadName)10.10s] %(module)-15.15s : %(funcName)s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            }
        },
    }
)
logger = logging.getLogger("app.root")
