from datetime import datetime

from app.models import CharityProject, Donation
from app.models.base_model import AbstractBase


def investment(
    target: CharityProject,
    sourses: Donation
) -> AbstractBase:
    """
    Перебирает открытые проекты/пожертвования,
    закрывает пожертвования/проекты при достижении лимита.
    При создании пожертвования перебирает открытые проекты.
    При создании проекта перебирает свободные пожертвования.
    """

    exit_objects = []
    for open_obj in sourses:
        """Перераспределяет средства между проектами и пожертвованиями."""
        append_obj = min(
            target.full_amount - target.invested_amount,
            open_obj.full_amount - open_obj.invested_amount
        )
        for object in target, open_obj:
            object.invested_amount += append_obj
            if object.invested_amount == open_obj.full_amount:
                object.fully_invested = True
                object.close_date = datetime.now()
        exit_objects.append(open_obj)
    return exit_objects
