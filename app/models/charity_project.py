from sqlalchemy import Column, String, Text
from app.models.base_model import AbstractBase


class CharityProject(AbstractBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def repr(self):
        return (
            f'Name: {self.name}, '
            f'{super().repr()}'
        )