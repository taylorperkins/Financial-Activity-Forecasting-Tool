from croniter import croniter
from datetime import datetime
from typing import AnyStr, Any

from pydantic import BaseModel, validator

from models.activity import ActivityModel


class RecurringActivityModel(BaseModel):
    cron_expression: AnyStr
    stop: datetime
    activity: ActivityModel

    class Config:
        extra = 'allow'

    @validator('stop', pre=True)
    def convert_datetime(cls, stop):
        return datetime.strptime(stop, '%Y-%m-%d')

    def __init__(self, **data: Any):
        super(RecurringActivityModel, self).__init__(**data)

        # once the model has been validated, we can hook into the date and cron to
        # create our schedule instance
        self.schedule = croniter(self.cron_expression, self.activity.date)

    def __iter__(self):
        return RecurringActivityModelIterator(self.copy(deep=True))


class RecurringActivityModelIterator:

    def __init__(self, model: RecurringActivityModel):
        self.model = model

    def __iter__(self):
        return self

    def __next__(self):
        if self.model.activity.date > self.model.stop:
            raise StopIteration

        self.model.activity.date = self.model.schedule.get_next(datetime)
        return self.model
