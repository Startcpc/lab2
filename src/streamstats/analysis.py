from collections import Counter
from typing import Iterable
from streamstats.constants import CRITICAL_LEVELS


def analys(events: Iterable) -> dict:
    """Составляем отчёт"""
    level_counts: Counter[str] = Counter()
    source_counts: Counter[str] = Counter()
    error_counts: Counter[str] = Counter()
    critical_counts: Counter[str] = Counter()
    total = 0
    first_event_time = None
    last_event_time = None
    for i in events:
        total += 1
        level_counts[i.level] += 1
        source_counts[i.source] += 1
        if i.level in CRITICAL_LEVELS:
            error_counts[i.source] += 1
            if i.level == "CRITICAL":
                critical_counts[i.source] += 1
        first_event_time = (
            min(first_event_time, i.timestamp) if first_event_time else i.timestamp
        )
        last_event_time = (
            max(last_event_time, i.timestamp) if last_event_time else i.timestamp
        )
    top_5 = sorted(
        error_counts.items(), key=lambda x: (x[1], critical_counts[x[0]]), reverse=True
    )[:5]
    return {
        "total": total,
        "levels": dict(level_counts),
        "source": dict(source_counts),
        "err_source": dict(error_counts),
        "top_5": top_5,
        "first_time_event": first_event_time,
        "last_time_event": last_event_time,
    }
