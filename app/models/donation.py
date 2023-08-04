from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)

from app.models.base_model import AbstractBase


class Donation(AbstractBase):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)

    def repr(self):
        return (
            f'User_id: {self.user_id}, '
            f'{super().repr()}'
        )
