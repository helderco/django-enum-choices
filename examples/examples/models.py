from django.db import models
from django.contrib.postgres.fields import ArrayField

from django_enum_choices.fields import EnumChoiceField

from .enumerations import MyEnum


# Model, containing a field with enumerations as choices
class MyModel(models.Model):
    enumerated_field = EnumChoiceField(enum_class=MyEnum)


# Model, containing a field with a array of enumerations (PostgreSQL specific)
class MyModelMultiple(models.Model):
    enumerated_field = ArrayField(
        base_field=EnumChoiceField(enum_class=MyEnum)
    )
