import logging
from logging import getLogger
from pydantic import ValidationError
from streamstats.errors import InvalidEventError, InvalidTimestampError

logging.basicConfig(
    filename="streamstats.log",
    level=logging.WARNING,
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logger = getLogger("streamstats")


def validation(
    error: Exception, file_name: str, line_num: int, skip_invalid: bool
) -> Exception | None:
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
