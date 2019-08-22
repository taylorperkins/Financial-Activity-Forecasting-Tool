
from typing import Union, List

from pydantic import BaseModel

from .recurring_activity import RecurringActivityModel
from .activity import ActivityModel


class ActivitiesModel(BaseModel):
    activities: List[Union[RecurringActivityModel, ActivityModel]]
