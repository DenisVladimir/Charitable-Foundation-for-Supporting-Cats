from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)

from app.core.db import Base


class Donation(Base):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)

    def __repr__(self):
        return (
            f"<User_id: {self.user_id}, "
            f"full_amount: {self.full_amount}, "
            f"invested_amount: {self.invested_amount}, "
            f"fully_invested: {self.fully_invested}>"
        )
