from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import CharityProject

from app.crud.base import CRUDBase


class CRUDCharityProject(CRUDBase):
    async def get_or_none(
        self,
        charity_id: int,
        session: AsyncSession,
    ) -> Optional[CharityProject]:
        """Возвращает объект CharityProject из БД по его id, либо возвращает None."""
        db_obj = await session.execute(
            select(self._model).where(self._model.id == charity_id)
        )
        return db_obj.scalars().first()

    async def exist_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> bool:
        """Проверяет существование полученного имени в БД, возвращает True/False."""
        db_project_id = await session.execute(
            select(select(self._model).where(self._model.name == project_name).exists())
        )
        return db_project_id.scalar()


charity_project_crud = CRUDCharityProject(CharityProject)
