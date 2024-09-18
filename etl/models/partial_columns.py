from functools import partial

from sqlalchemy import Column

NotNullColumn = partial(Column, nullable=False)

__all__ = ["NotNullColumn"]
