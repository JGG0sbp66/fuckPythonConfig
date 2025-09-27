# 存放各种读取工具
import os
import re
import tomllib

from .exceptions import FileNotFoundError, TOMLReadError


def is_env_var(value: str, ENV_VAR_REGEX: str = r"\$\{[^}]*\}") -> bool:
    """使用正则表达式判断是否为${value}格式"""
    return bool(re.fullmatch(ENV_VAR_REGEX, value))


def read_toml(file_path: str) -> dict:
    """使用tomllib读取TOML文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Can not find TOML file", file_path)
    try:
        with open(file_path, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        raise TOMLReadError("Failed to read TOML file", file_path) from e


def get_env_var(env_key: str) -> str:
    """使用os读取环境变量"""
    return os.getenv(env_key, "")
