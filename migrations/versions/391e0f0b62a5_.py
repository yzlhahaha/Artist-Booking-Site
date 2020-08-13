"""empty message

Revision ID: 391e0f0b62a5
Revises: 03b1ff19c73a
Create Date: 2020-08-11 21:02:32.704781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391e0f0b62a5'
down_revision = '03b1ff19c73a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=False))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'genres')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'start_time')
    op.drop_column('Show', 'artist_id')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
