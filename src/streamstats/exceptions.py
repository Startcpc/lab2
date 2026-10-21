from logging import getLogger, warning
from .errors import InvalidEventError, InvalidTimestampError
logger = getLogger("streamstats")
def validation(error: Exception, file_name: str, line_num: int, skip_invalid: bool) -> Exception | None:
    if skip_invalid:
        warning(f"Пропущена строка {line_num} в файле {file_name}")
        return None
    if "timestamp" in str(error):
        return InvalidTimestampError(f"Файл: {file_name}, Строка: {line_num}. Ошибка: InvalidTimestampError -> Неверная временная метка")
    return InvalidEventError(f"Файл: {file_name}, Строка: {line_num}. Ошибка: InvalidEventError -> Неверное событие")
