from django.apps import apps

"""This utils file, will help to create some helper method
    that will help to get only models we want in the whole project"""

def get_all_custom_models():
    default_models = ["ContentType", "Session", "Group", "Permission", "LogEntry"]
    custom_models = []

    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)
    return custom_models