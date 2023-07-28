from typing import List, Optional, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import investing_sevice
from app.models import CharityProject, Donation, User
# from app.core.services import set_user_service
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException


class CRUDBase:
    def __init__(self, model):
        self._model = model

    async def get_all(
        self,
        session: AsyncSession,
    ) -> List[Union[CharityProject, Donation]]:
        """Возвращает все объекты из БД текущей модели."""
        db_objs = await session.execute(select(self._model))
        return db_objs.scalars().all()

    async def create(
        self,
        request_obj,
        session: AsyncSession,
        user: Optional[User] = None,
        commit_flag: bool = True,
    ) -> Union[CharityProject, Donation]:

        """Создает объект текущей модели."""
        request_object = request_obj.dict()
        if user is not None:
            request_object["user_id"] = user.id
        db_obj = self._model(**request_object)
        session.add(db_obj)

        if commit_flag:
            await session.commit()
        else:
            await session.flush()  # Используем метод flush() вместо commit(), чтобы временно сохранить изменения без фиксации.

        await session.refresh(db_obj)
        return db_obj

    async def get_by_id(
        self,
        project_id: int,
        session: AsyncSession
    ) -> CharityProject:
        """Возвращает объект CharityProject по его id, либо выбрасывает ошибку"""
        project = await self.get_or_none(project_id, session)
        if project is None:
            raise HTTPException(status_code=404, detail="Проект не найден!")
        return project

    async def update(
        self,
        db_obj: CharityProject,
        obj_in,
        session: AsyncSession,
    ) -> CharityProject:
        """Обновляет объект CharityProject и возвращает обновленный объект."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict()
        for field in obj_data:
            if field in update_data and update_data[field] is not None:
                setattr(db_obj, field, update_data[field])
        db_obj = investing_sevice.set_close(db_obj)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj: CharityProject,
        session: AsyncSession,
    ) -> CharityProject:
        """Удаляет объект CharityProject по его id."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj
