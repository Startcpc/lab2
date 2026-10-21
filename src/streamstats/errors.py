class StreamStatsError(Exception):
    """Родитель ошибок"""
    pass

class UnsupportedFormatError(StreamStatsError):
    """Неподдерживаемый формат"""
    pass

class InvalidEventError(StreamStatsError):
    """Некорректное событие"""
    pass

class InvalidTimestampError(InvalidEventError):
    """Некорректная временная метка"""
    pass

class ConfigurationError(StreamStatsError):
    """Ошибка конфигурации CLI"""
    pass
