from .constants import CRITICAL_LEVELS


def analys(events: list, skipped_lines: int = 0) -> dict:
    """Анализ событий"""
    levels: dict[str, int] = {}
    source: dict[str, int] = {}
    err_source: dict[str, int] = {}
    timestamps: list = []
    for i in events:
        timestamps.append(i.timestamp)
        levels[i.level] = levels.get(i.level, 0) + 1
        source[i.source] = source.get(i.source, 0) + 1
        if i.level in CRITICAL_LEVELS:
            err_source[i.source] = err_source.get(i.source, 0) + 1
    top_5 = sorted(err_source.items(), key=lambda x: x[1], reverse=True)[:5]
    return {
        "total": len(events),
        "levels": levels,
        "source": source,
        "err_source": err_source,
        "top_5": top_5,
        "first_time_event": min(timestamps) if timestamps else None,
        "last_time_event": max(timestamps) if timestamps else None,
        "skipped_lines": skipped_lines,
    }
