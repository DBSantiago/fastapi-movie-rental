"""Add seasons and episodes tables

Revision ID: 76d0399a75dd
Revises: de19628fbdad
Create Date: 2022-10-14 20:27:25.715310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76d0399a75dd'
down_revision = 'de19628fbdad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('series_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['series_id'], ['films.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('series_id', 'number', name='unique_season_number')
    )
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('season_id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['season_id'], ['seasons.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('season_id', 'number', name='unique_episode_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episodes')
    op.drop_table('seasons')
    # ### end Alembic commands ###