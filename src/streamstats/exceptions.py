from logging import getLogger
from pydantic import ValidationError
from .errors import InvalidEventError, InvalidTimestampError

logger = getLogger("streamstats")


def validation(
    error: Exception, file_name: str, line_num: int, skip_invalid: bool
) -> Exception | None:
    """Тип ошибки выдает"""
    if skip_invalid:
        logger.warning(f"Пропущена строка {line_num} в файле {file_name}")
        return None

    if isinstance(error, ValidationError):
        for err in error.errors():
            if "timestamp" in err["loc"]:
                return InvalidTimestampError(
                    f"Файл: {file_name}, Строка: {line_num}. Ошибка: InvalidTimestampError -> Неверная временная метка"
                )
        return InvalidEventError(
            f"Файл: {file_name}, Строка: {line_num}. Ошибка: InvalidEventError -> Неверное событие"
        )
    return InvalidEventError(
        f"Файл: {file_name}, Строка: {line_num}. Ошибка: InvalidEventError -> Неизвестная ошибка"
    )
