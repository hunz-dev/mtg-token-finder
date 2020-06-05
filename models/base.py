from peewee import Model
from . import database


# Create a base-class all models will inherit
class BaseModel(Model):
    class Meta:
        database = database
