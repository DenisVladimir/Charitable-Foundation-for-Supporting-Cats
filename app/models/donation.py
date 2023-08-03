from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)

from app.models.base_model import BaseModel


class Donation(BaseModel):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)

    def __repr__(self):
        base_repr = super().__repr__()
        return (
            f'<User_id: {self.user_id}, '
            f'{base_repr},>'
        )
