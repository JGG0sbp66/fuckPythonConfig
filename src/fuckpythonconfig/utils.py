# 存放各种读取工具
import re
import os
import tomllib

from .exceptions import FileNotFoundError

ENV_VAR_REGEX = r'\$\{[^}]*\}'

def is_env_var(value: str) -> bool:
    """使用正则表达式判断是否为${value}格式"""
    return bool(re.fullmatch(ENV_VAR_REGEX, value))

def read_toml(file_path: str) -> dict:
    """使用tomllib读取TOML文件"""
    if not os.path.exists(file_path):
        raise FileNotFoundError("Can not find TOML file", file_path, None)
    with open(file_path, "rb") as f:
        return tomllib.load(f)

def get_env_var(env_key: str) -> str:
    """使用os读取环境变量"""
    return os.getenv(env_key, "")