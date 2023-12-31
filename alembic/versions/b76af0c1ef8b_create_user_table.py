"""create user table

Revision ID: b76af0c1ef8b
Revises: 
Create Date: 2023-08-16 05:39:31.197046

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b76af0c1ef8b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('first_name', sa.String(length=256), nullable=False),
    sa.Column('last_name', sa.String(length=256), nullable=False),
    sa.Column('email_address', sa.String(), nullable=False),
    sa.Column('telephone_number', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), server_default='user', nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email_address'), 'user', ['email_address'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_telephone_number'), 'user', ['telephone_number'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_telephone_number'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email_address'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
