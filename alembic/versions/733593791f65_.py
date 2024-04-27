"""empty message

Revision ID: 733593791f65
Revises: 3922d5c85ec8
Create Date: 2024-04-26 22:46:33.643594

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '733593791f65'
down_revision: Union[str, None] = '3922d5c85ec8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracts',
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('dmtt_id', sa.Integer(), nullable=True),
    sa.Column('excel_url', sa.String(length=255), nullable=True),
    sa.Column('active_sheet_name', sa.String(length=31), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['dmtt_id'], ['dmtt.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contracts')
    # ### end Alembic commands ###