from typing import Union
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import CharityProject, Donation
from datetime import datetime


def investment(
    target: Union[CharityProject, Donation],
    sourses: Union[CharityProject, Donation],
) -> None:
    """
    Перебирает открытые проекты/пожертвования,
    закрывает пожертвования/проекты при достижении лимита.
    При создании пожертвования перебирает открытые проекты.
    При создании проекта перебирает свободные пожертвования.

    :param new_obj: - только что созданное пожертвование/проект
    :param model:  - модель, открытые объекты которой мы будем перебирать.
    """
    data_mass = [] # выходной массив данных открытых проектов
    for open_obj in sourses:
        #targer, open_obj = reinvestment(targer, open_obj)     
        """Перераспределяет средства между проектами и пожертвованиями."""
        # сколько не хватает для закрытия нового проекта
        to_close_new_obj = target.full_amount - target.invested_amount
        # Сколько осталось в открытом пожертвовании
        to_close_open_obj = open_obj.full_amount - open_obj.invested_amount
        append_obj = min(to_close_new_obj, to_close_open_obj)
        target.invested_amount += append_obj
        open_obj.invested_amount += append_obj        
        if open_obj.invested_amount == open_obj.full_amount:
            """Закрывает объект и добавляет дату закрытия."""
            open_obj.fully_invested = True
            open_obj.close_date = datetime.now()
        data_mass.append(open_obj)
        if target.invested_amount == target.full_amount:
            """Закрывает объект и добавляет дату закрытия."""
            target.fully_invested = True
            target.close_date = datetime.now()
            break
    return target, data_mass
