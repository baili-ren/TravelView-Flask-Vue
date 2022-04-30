"""four

Revision ID: 505d1cefc15d
Revises: 445a0b6d2c2e
Create Date: 2022-04-28 10:53:35.584675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '505d1cefc15d'
down_revision = '445a0b6d2c2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provincescenic',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('provinceName', sa.String(length=200), nullable=False),
    sa.Column('ScenicName', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table_comment(
        'hotcityplace',
        existing_comment='热门城市的热门景点\\r\\n',
        schema=None
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table_comment(
        'hotcityplace',
        '热门城市的热门景点\\r\\n',
        existing_comment=None,
        schema=None
    )
    op.drop_table('provincescenic')
    # ### end Alembic commands ###
