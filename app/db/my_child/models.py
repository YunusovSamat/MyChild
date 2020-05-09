from tortoise import fields
from tortoise import models

STR_MAX_LENGTH = 50
LINK_MAX_LENGTH = 150
PASSW_MAX_LENGTH = 100
COMMENT_MAX_LENGTH = 200


class Educator(models.Model):
    educator_id = fields.UUIDField(pk=True)
    username = fields.CharField(max_length=STR_MAX_LENGTH)
    password = fields.CharField(max_length=PASSW_MAX_LENGTH)
    name = fields.CharField(max_length=STR_MAX_LENGTH)
    surname = fields.CharField(max_length=STR_MAX_LENGTH)
    patronymic = fields.CharField(max_length=STR_MAX_LENGTH)

    children: fields.ReverseRelation["Child"]
    foods: fields.ReverseRelation["Food"]


class Child(models.Model):
    child_id = fields.UUIDField(pk=True)
    educator: fields.ForeignKeyRelation[Educator] = fields.ForeignKeyField(
        "my_child.Educator",
        related_name="children",
        on_delete=fields.SET_NULL,
        null=True,
    )
    age = fields.IntField(null=True)
    photo_link = fields.CharField(LINK_MAX_LENGTH, null=True)
    blood_type = fields.CharField(STR_MAX_LENGTH, null=True)
    group = fields.CharField(STR_MAX_LENGTH, null=True)
    locker_num = fields.CharField(STR_MAX_LENGTH, null=True)
    name = fields.CharField(STR_MAX_LENGTH)
    surname = fields.CharField(STR_MAX_LENGTH)
    patronymic = fields.CharField(STR_MAX_LENGTH)

    parents: fields.ReverseRelation["Parent"]
    events: fields.ReverseRelation["Event"]


class Parent(models.Model):
    parent_id = fields.UUIDField(pk=True)
    child: fields.ForeignKeyRelation[Child] = fields.ForeignKeyField(
        "my_child.Child", related_name="parents", on_delete=fields.CASCADE, null=True
    )
    username = fields.CharField(max_length=STR_MAX_LENGTH)
    password = fields.CharField(max_length=PASSW_MAX_LENGTH)
    relation_degree = fields.CharField(max_length=STR_MAX_LENGTH, null=True)
    phone = fields.CharField(max_length=STR_MAX_LENGTH, null=True)
    photo_link = fields.CharField(LINK_MAX_LENGTH, null=True)
    name = fields.CharField(STR_MAX_LENGTH, null=True)
    surname = fields.CharField(STR_MAX_LENGTH, null=True)
    patronymic = fields.CharField(STR_MAX_LENGTH, null=True)


class Event(models.Model):
    event_id = fields.UUIDField(pk=True)
    child: fields.ForeignKeyRelation[Child] = fields.ForeignKeyField(
        "my_child.Child", related_name="events", on_delete=fields.CASCADE
    )
    date = fields.DateField()
    has_come = fields.CharField(STR_MAX_LENGTH, null=True)
    has_gone = fields.CharField(STR_MAX_LENGTH, null=True)
    asleep = fields.CharField(STR_MAX_LENGTH, null=True)
    awoke = fields.CharField(STR_MAX_LENGTH, null=True)
    comment = fields.CharField(COMMENT_MAX_LENGTH, null=True)

    meals: fields.ReverseRelation["Meal"]


class Meal(models.Model):
    meal_id = fields.UUIDField(pk=True)
    event: fields.ForeignKeyRelation[Event] = fields.ForeignKeyField(
        "my_child.Event", related_name="meals", on_delete=fields.CASCADE
    )
    type = fields.IntField()

    rations: fields.ReverseRelation["Ration"]


class Food(models.Model):
    food_id = fields.UUIDField(pk=True)
    educator: fields.ForeignKeyRelation[Educator] = fields.ForeignKeyField(
        "my_child.Educator", related_name="events", on_delete=fields.SET_NULL, null=True
    )
    name = fields.CharField(STR_MAX_LENGTH)

    rations: fields.ReverseRelation["Ration"]


class Ration(models.Model):
    ration_id = fields.UUIDField(pk=True)
    meal: fields.ForeignKeyRelation[Meal] = fields.ForeignKeyField(
        "my_child.Meal",
        related_name="meal_rations",
        null=True,
        on_delete=fields.CASCADE,
    )
    food: fields.OneToOneRelation[Food] = fields.OneToOneField(
        "my_child.Food", related_name="food_rations", on_delete=fields.CASCADE
    )
    denial = fields.BooleanField()
