"""Add termination_reason to sessions

Revision ID: 044ac7b24ce2
Revises: 99eb6904254e
Create Date: 2020-07-23 20:18:49.021978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '044ac7b24ce2'
down_revision = '99eb6904254e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('termination_reason', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session', 'termination_reason')
    # ### end Alembic commands ###
