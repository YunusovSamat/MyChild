from tortoise import fields, models


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
    educator_id: fields.ForeignKeyRelation[Educator] = fields.ForeignKeyField(
        "my_child.Educator", related_name="children")
    age = fields.IntField()
    photo_type = fields.CharField(LINK_MAX_LENGTH)
    blood_type = fields.CharField(STR_MAX_LENGTH)
    group = fields.CharField(STR_MAX_LENGTH)
    locker_num = fields.CharField(STR_MAX_LENGTH)
    name = fields.CharField(STR_MAX_LENGTH)
    surname = fields.CharField(STR_MAX_LENGTH)
    patronymic = fields.CharField(STR_MAX_LENGTH)

    parents: fields.ReverseRelation["Parent"]
    events: fields.ReverseRelation["Event"]


class Parent(models.Model):
    parent_id = fields.UUIDField(pk=True)
    child_id: fields.ForeignKeyRelation[Child] = fields.ForeignKeyField(
        "my_child.Child", related_name="parents")
    username = fields.CharField(max_length=STR_MAX_LENGTH)
    password = fields.CharField(max_length=PASSW_MAX_LENGTH)
    relation_degree = fields.CharField(max_length=STR_MAX_LENGTH)
    phone = fields.IntField()
    photo_type = fields.CharField(LINK_MAX_LENGTH)
    name = fields.CharField(STR_MAX_LENGTH)
    surname = fields.CharField(STR_MAX_LENGTH)
    patronymic = fields.CharField(STR_MAX_LENGTH)


class Event(models.Model):
    event_id = fields.UUIDField(pk=True)
    child_id: fields.ForeignKeyRelation[Child] = fields.ForeignKeyField(
        "my_child.Child", related_name="events")
    date = fields.DateField()
    has_come = fields.CharField(STR_MAX_LENGTH)
    has_gone = fields.CharField(STR_MAX_LENGTH)
    asleep = fields.CharField(STR_MAX_LENGTH)
    awoke = fields.CharField(STR_MAX_LENGTH)
    comment = fields.CharField(COMMENT_MAX_LENGTH)

    meals: fields.ReverseRelation["Meal"]


class Meal(models.Model):
    meal_id = fields.UUIDField(pk=True)
    event_id: fields.ForeignKeyRelation[Event] = fields.ForeignKeyField(
        "my_child.Event", related_name="meals")
    type = fields.IntField()

    rations: fields.ReverseRelation["Ration"]


class Food(models.Model):
    food_id = fields.UUIDField(pk=True)
    educator_id: fields.ForeignKeyRelation[Educator] = fields.ForeignKeyField(
        "my_child.Educator", related_name="events")
    name = fields.CharField(STR_MAX_LENGTH)

    rations: fields.ReverseRelation["Ration"]


class Ration(models.Model):
    ration_id = fields.UUIDField(pk=True)
    meal_id: fields.ForeignKeyRelation[Meal] = fields.ForeignKeyField(
        "my_child.Meal", related_name="meal_rations")
    food_id: fields.OneToOneRelation[Food] = fields.OneToOneField(
        "my_child.Food", related_name="food_rations")
    denial = fields.BooleanField()