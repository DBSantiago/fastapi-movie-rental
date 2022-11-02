"""Add customer table

Revision ID: 77648b0a8f67
Revises: 4d8bbcd16dfc
Create Date: 2022-10-13 23:18:42.256571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77648b0a8f67'
down_revision = '4d8bbcd16dfc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('last_name', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###