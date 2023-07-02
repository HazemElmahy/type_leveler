"""init tables

Revision ID: b82fc066abc3
Revises: 
Create Date: 2023-07-02 21:03:44.920117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b82fc066abc3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "speed",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('speed', sa.Integer),
        sa.Column('state', sa.Integer),
    )
    op.create_table(
        "accuracy",
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('accuracy', sa.Float),
        sa.Column('state', sa.Integer),
    )


def downgrade() -> None:
    pass
