"""two

Revision ID: 5f056f77d724
Revises: 55666d880991
Create Date: 2022-04-26 01:24:31.215323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f056f77d724'
down_revision = '55666d880991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('tt', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'tt')
    # ### end Alembic commands ###
