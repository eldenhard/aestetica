"""init

Revision ID: 77c6160bb92b
Revises: 
Create Date: 2023-09-01 11:38:36.266765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '77c6160bb92b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('name', sa.String(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('filials',
    sa.Column('name', sa.String(length=50), autoincrement=False, nullable=False),
    sa.Column('db_address', sa.String(length=15), nullable=True),
    sa.Column('db_port', sa.String(length=5), nullable=True),
    sa.Column('db_name', sa.String(length=50), nullable=True),
    sa.Column('db_user', sa.String(length=150), nullable=True),
    sa.Column('db_password', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('name', sa.String(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('services',
    sa.Column('code', sa.String(length=20), autoincrement=False, nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('is_submit', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('code'),
    sa.UniqueConstraint('code')
    )
    op.create_table('staff',
    sa.Column('name', sa.String(length=150), autoincrement=False, nullable=False),
    sa.Column('role', sa.String(length=150), nullable=False),
    sa.Column('is_new', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role'], ['roles.name'], ),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bonuses',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_begin', sa.Date(), nullable=False),
    sa.Column('date_end', sa.Date(), nullable=False),
    sa.Column('staff', sa.String(length=150), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['staff'], ['staff.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('staff', 'date_begin', 'date_end', name='staff_dates_uc')
    )
    op.create_table('consumables',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('service', sa.String(length=20), nullable=False),
    sa.Column('staff', sa.String(length=150), nullable=False),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['service'], ['services.code'], ),
    sa.ForeignKeyConstraint(['staff'], ['staff.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('staff', 'service', name='staff_service_uc')
    )
    op.create_table('salary',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('staff', sa.String(length=150), nullable=False),
    sa.Column('department', sa.String(length=50), nullable=False),
    sa.Column('fix', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['department'], ['departments.name'], ),
    sa.ForeignKeyConstraint(['staff'], ['staff.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('salary_grid',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('limit', sa.Float(), nullable=False),
    sa.Column('percent', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['salary'], ['salary.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('salary_grid')
    op.drop_table('salary')
    op.drop_table('consumables')
    op.drop_table('bonuses')
    op.drop_table('staff')
    op.drop_table('services')
    op.drop_table('roles')
    op.drop_table('filials')
    op.drop_table('departments')
    # ### end Alembic commands ###
