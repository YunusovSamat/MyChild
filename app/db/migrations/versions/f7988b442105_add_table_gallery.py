"""Add table gallery

Revision ID: f7988b442105
Revises: 4a2002183d60
Create Date: 2020-05-24 20:13:49.981090

Doc: https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script
"""
from sqlalchemy.dialects.postgresql import UUID
from alembic import op
import sqlalchemy as sa


revision = 'f7988b442105'
down_revision = '4a2002183d60'
branch_labels = None
depends_on = None

LINK_MAX_LENGTH = 150
COMMENT_MAX_LENGTH = 200


def create_gallery():
    op.create_table(
        "gallery",
        sa.Column("gallery_id", UUID, primary_key=True),
        sa.Column(
            "educator_id",
            UUID,
            sa.ForeignKey("educator.educator_id", ondelete="SET NULL"),
        ),
        sa.Column("photo_link", sa.String(LINK_MAX_LENGTH)),
        sa.Column("description", sa.String(COMMENT_MAX_LENGTH)),
        sa.Column("timestamp", sa.TIMESTAMP)
    )


def upgrade():
    create_gallery()


def downgrade():
    op.drop_table("gallery")
