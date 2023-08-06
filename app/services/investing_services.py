from datetime import datetime
from typing import List, Union

from app.crud.base import CRUDBase
from app.crud.charity_project import CRUDCharityProject
from app.crud.donation import CRUDDonation


def investment(
    target: Union[CRUDCharityProject, CRUDDonation],
    sourses: List[Union[CRUDCharityProject, CRUDDonation]]
) -> List[CRUDBase]:
    """
    Перебирает открытые проекты/пожертвования,
    закрывает пожертвования/проекты при достижении лимита.
    При создании пожертвования перебирает открытые проекты.
    При создании проекта перебирает свободные пожертвования.
    """
    changed_objects = []
    for open_obj in sourses:
        """Перераспределяет средства между проектами и пожертвованиями."""
        append_obj = min(
            target.full_amount - target.invested_amount,
            open_obj.full_amount - open_obj.invested_amount
        )
        if append_obj == 0:
            break
        for object in target, open_obj:
            object.invested_amount += append_obj
            if object.invested_amount == open_obj.full_amount:
                object.fully_invested = True
                object.close_date = datetime.now()
            if object in sourses:
                changed_objects.append(object)
    return changed_objects
