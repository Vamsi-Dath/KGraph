from pydantic import BaseModel
from typing import Optional

class Chunk(BaseModel):
    id: int
    """The unique identifier of the chunk."""

    text: str
    """The text of the chunk."""
    