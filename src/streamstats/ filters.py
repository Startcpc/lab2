from datetime import datetime
from typing import Iterable
from .models import Event


def filter_by_time(events: Iterable[Event], start: datetime, end: datetime):
    """фильтрует события по времени"""
    for event in events:
        if start <= event.timestamp <= end:
            yield event


def filter_by_level(events: Iterable[Event], level: str):
    """фильтрует события по уровню"""
    for event in events:
        if event.level == level:
            yield event


def filter_by_source(events: Iterable[Event], source: str):
    """фильтрует события по источнику"""
    for event in events:
        if event.source == source:
            yield event
