"""Base models

Revision ID: 4a2002183d60
Revises: 
Create Date: 2020-05-03 20:05:54.418690

Doc: https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

revision = "4a2002183d60"
down_revision = None
branch_labels = None
depends_on = None


STR_MAX_LENGTH = 50
LINK_MAX_LENGTH = 150
PASSW_MAX_LENGTH = 100
COMMENT_MAX_LENGTH = 200


def create_educator_table():
    op.create_table(
        "educator",
        sa.Column("educator_id", UUID, primary_key=True),
        sa.Column("username", sa.String(STR_MAX_LENGTH)),
        sa.Column("password", sa.String(PASSW_MAX_LENGTH)),
        sa.Column("name", sa.String(STR_MAX_LENGTH)),
        sa.Column("surname", sa.String(STR_MAX_LENGTH)),
        sa.Column("patronymic", sa.String(STR_MAX_LENGTH)),
    )


def create_child_table():
    op.create_table(
        "child",
        sa.Column("child_id", UUID, primary_key=True),
        sa.Column(
            "educator_id",
            UUID,
            sa.ForeignKey("educator.educator_id", ondelete="SET NULL"),
        ),
        sa.Column("age", sa.Integer, sa.CheckConstraint("age > 2 and age < 7")),
        sa.Column("photo_link", sa.String(LINK_MAX_LENGTH)),
        sa.Column("blood_type", sa.String(STR_MAX_LENGTH)),
        sa.Column("group", sa.String(STR_MAX_LENGTH)),
        sa.Column("locker_num", sa.String(STR_MAX_LENGTH)),
        sa.Column("name", sa.String(STR_MAX_LENGTH)),
        sa.Column("surname", sa.String(STR_MAX_LENGTH)),
        sa.Column("patronymic", sa.String(STR_MAX_LENGTH)),
    )


def create_bill_table():
    op.create_table(
        "bill",
        sa.Column("bill_id", UUID, primary_key=True),
        sa.Column(
            "child_id", UUID, sa.ForeignKey("child.child_id", ondelete="CASCADE")
        ),
        sa.Column("theme", sa.String(STR_MAX_LENGTH)),
        sa.Column("sum", sa.Integer, sa.CheckConstraint("sum >= 0")),
        sa.Column("status", sa.Boolean),
        sa.Column("comment", sa.String(COMMENT_MAX_LENGTH)),
    )


def create_parent_table():
    op.create_table(
        "parent",
        sa.Column("parent_id", UUID, primary_key=True),
        sa.Column(
            "child_id", UUID, sa.ForeignKey("child.child_id", ondelete="SET NULL")
        ),
        sa.Column("username", sa.String(STR_MAX_LENGTH)),
        sa.Column("password", sa.String(PASSW_MAX_LENGTH)),
        sa.Column("relation_degree", sa.String(STR_MAX_LENGTH)),
        sa.Column("phone", sa.String(STR_MAX_LENGTH)),
        sa.Column("photo_link", sa.String(LINK_MAX_LENGTH)),
        sa.Column("name", sa.String(STR_MAX_LENGTH)),
        sa.Column("surname", sa.String(STR_MAX_LENGTH)),
        sa.Column("patronymic", sa.String(STR_MAX_LENGTH)),
    )


def create_event_table():
    op.create_table(
        "event",
        sa.Column("event_id", UUID, primary_key=True),
        sa.Column(
            "child_id", UUID, sa.ForeignKey("child.child_id", ondelete="CASCADE")
        ),
        sa.Column("date", sa.DATE),
        sa.Column("has_come", sa.String(STR_MAX_LENGTH)),
        sa.Column("has_gone", sa.String(STR_MAX_LENGTH)),
        sa.Column("asleep", sa.String(STR_MAX_LENGTH)),
        sa.Column("awoke", sa.String(STR_MAX_LENGTH)),
        sa.Column("comment", sa.String(COMMENT_MAX_LENGTH)),
    )


def create_meal_table():
    op.create_table(
        "meal",
        sa.Column("meal_id", UUID, primary_key=True),
        sa.Column(
            "event_id", UUID, sa.ForeignKey("event.event_id", ondelete="CASCADE")
        ),
        sa.Column("type", sa.Integer, sa.CheckConstraint("type >= 1 and type <= 3")),
    )


def create_food_table():
    op.create_table(
        "food",
        sa.Column("food_id", UUID, primary_key=True),
        sa.Column(
            "educator_id",
            UUID,
            sa.ForeignKey("educator.educator_id", ondelete="SET NULL"),
        ),
        sa.Column("name", sa.String(STR_MAX_LENGTH)),
    )


def create_ration_table():
    op.create_table(
        "ration",
        sa.Column("ration_id", UUID, primary_key=True),
        sa.Column("meal_id", UUID, sa.ForeignKey("meal.meal_id", ondelete="CASCADE")),
        sa.Column("food_id", UUID, sa.ForeignKey("food.food_id", ondelete="CASCADE")),
        sa.Column("denial", sa.Boolean),
    )


def upgrade():
    create_educator_table()
    create_child_table()
    create_bill_table()
    create_parent_table()
    create_event_table()
    create_meal_table()
    create_food_table()
    create_ration_table()


def downgrade():
    op.drop_table("ration")
    op.drop_table("food")
    op.drop_table("meal")
    op.drop_table("event")
    op.drop_table("parent")
    op.drop_table("bill")
    op.drop_table("child")
    op.drop_table("educator")
