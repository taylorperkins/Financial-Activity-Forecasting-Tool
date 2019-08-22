from datetime import datetime
from typing import AnyStr

from pydantic import BaseModel, validator

from conf import YEAR_FMT


class ActivityModel(BaseModel):
    type = 'activity'

    date: datetime
    name: AnyStr = "Activity"

    @validator('date', pre=True)
    def convert_datetime(cls, _date):
        return datetime.strptime(_date, YEAR_FMT)
