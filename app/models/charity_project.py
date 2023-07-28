from sqlalchemy import Column, String, Text

from app.core.db import Base


class CharityProject(Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f"<Name: {self.name}, "
            f"full_amount: {self.full_amount}, "
            f"invested_amount: {self.invested_amount}, "
            f"fully_invested: {self.fully_invested}>"
        )
