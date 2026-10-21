class StreamStatsError(Exception):
    """Родитель ошибок"""

class UnsupportedFormatError(StreamStatsError):
    """Неподдерживаемый формат"""

class InvalidEventError(StreamStatsError):
    """Некорректное событие"""

class InvalidTimestampError(InvalidEventError):
    """Некорректная временная метка"""

class ConfigurationError(StreamStatsError):
    """Ошибка конфигурации CLI"""
