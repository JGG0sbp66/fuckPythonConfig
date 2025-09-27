# 存放各种读取工具
import os
import re
import tomllib
from typing import IO

from dotenv import load_dotenv

from .exceptions import FileNotFoundError, TOMLReadError


def read_toml(file_path: str) -> dict:
    """使用tomllib读取TOML文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Can not find TOML file", file_path)
    try:
        with open(file_path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        raise TOMLReadError("Failed to read TOML file", file_path) from e


def read_env(
    dotenv_path: str | None = None,
    stream: IO[str] | None = None,
    verbose: bool = False,
    override: bool = False,
    interpolate: bool = True,
    encoding: str | None = "utf-8",
) -> bool:
    """感谢python-dotenv库实现了非常成熟且高级的读取env的方法, mua~"""
    return load_dotenv(
        dotenv_path=dotenv_path,
        stream=stream,
        verbose=verbose,
        override=override,
        interpolate=interpolate,
        encoding=encoding,
    )


def is_env_var(value: str, ENV_VAR_REGEX: str = r"\$\{[^}]*\}") -> bool:
    """使用正则表达式判断是否为${value}格式"""
    return bool(re.fullmatch(ENV_VAR_REGEX, value))


def get_env_var(env_key: str) -> str:
    """使用os读取环境变量"""
    return os.getenv(env_key, "")
