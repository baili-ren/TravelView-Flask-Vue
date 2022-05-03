"""nine

Revision ID: 8102c4b5cdc2
Revises: fbbf92d806d4
Create Date: 2022-04-29 06:25:19.562037

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8102c4b5cdc2'
down_revision = 'fbbf92d806d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scenictype', sa.Column('scenicType', sa.String(length=200), nullable=False))
    op.add_column('scenictype', sa.Column('scenicNum', sa.String(length=200), nullable=False))
    op.drop_column('scenictype', 'ScenicType')
    op.drop_column('scenictype', 'ScenicNum')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('scenictype', sa.Column('ScenicNum', mysql.VARCHAR(length=200), nullable=False))
    op.add_column('scenictype', sa.Column('ScenicType', mysql.VARCHAR(length=200), nullable=False))
    op.drop_column('scenictype', 'scenicNum')
    op.drop_column('scenictype', 'scenicType')
    # ### end Alembic commands ###