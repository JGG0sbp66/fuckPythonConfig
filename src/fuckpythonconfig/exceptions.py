# 存放各种自定义异常

class ConfigReadError(Exception):
    """配置文件读取错误异常"""

    def __init__(self, message: str, file_path: str, original_error: Exception | None):
        self.message = message
        self.file_path = file_path
        self.original_error = original_error
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        msg = f"{self.message} (file_path: {self.file_path})"
        if self.original_error:
            msg += f" - original_error: {self.original_error}"
        return msg

class FileNotFoundError(ConfigReadError):
    pass

class TOMLReadError(ConfigReadError):
    pass

class ENVReadError(ConfigReadError):
    pass