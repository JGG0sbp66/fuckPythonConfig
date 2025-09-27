# TODO: 计划在这里编写核心功能
"""
TODO: 最暴力的实现逻辑就是
1. 读取toml
2. 使用for循环去遍历toml
3. 使用is_env_var()去判断当前key的value是不是符合${...}格式的
4. 如果是, 我就用os.getenv去读取, 然后替换掉
"""
