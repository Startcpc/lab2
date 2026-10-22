from typing import Annotated
from pydantic import AwareDatetime, BaseModel, StringConstraints
from .constants import VALID_LEVEL


class Event(BaseModel):
    """Правила события"""

    timestamp: AwareDatetime
    level: VALID_LEVEL
    source: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    message: str
