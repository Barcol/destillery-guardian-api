"""added time interval to session

Revision ID: 99eb6904254e
Revises: 5a9793d6fead
Create Date: 2020-07-12 16:19:27.877940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99eb6904254e'
down_revision = '5a9793d6fead'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('time_interval', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session', 'time_interval')
    # ### end Alembic commands ###