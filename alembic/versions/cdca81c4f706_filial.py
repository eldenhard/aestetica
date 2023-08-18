"""filial

Revision ID: cdca81c4f706
Revises: 8c09790bf423
Create Date: 2023-08-15 12:26:28.076540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdca81c4f706'
down_revision: Union[str, None] = '8c09790bf423'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filials', sa.Column('db_address', sa.String(length=15), nullable=True))
    op.add_column('filials', sa.Column('db_port', sa.String(length=5), nullable=True))
    op.add_column('filials', sa.Column('db_name', sa.String(length=50), nullable=True))
    op.add_column('filials', sa.Column('db_user', sa.String(length=150), nullable=True))
    op.add_column('filials', sa.Column('db_password', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('filials', 'db_password')
    op.drop_column('filials', 'db_user')
    op.drop_column('filials', 'db_name')
    op.drop_column('filials', 'db_port')
    op.drop_column('filials', 'db_address')
    # ### end Alembic commands ###
