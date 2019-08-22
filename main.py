from yaml import load, Loader

from models import ActivitiesModel


if __name__ == '__main__':
    with open('./example.yaml') as f:
        data = load(f, Loader=Loader)

    activities = ActivitiesModel(**data)

    for activity in activities.activities:
        for step in activity:
            print(step)
