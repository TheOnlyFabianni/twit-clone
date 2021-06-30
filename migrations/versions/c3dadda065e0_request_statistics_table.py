"""Request statistics table

Revision ID: c3dadda065e0
Revises: c4bb6e01d5b7
Create Date: 2021-06-30 13:07:37.426187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3dadda065e0'
down_revision = 'c4bb6e01d5b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('path', sa.String(length=255), nullable=True),
    sa.Column('method', sa.String(length=8), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('browser', sa.String(length=20), nullable=True),
    sa.Column('platform', sa.String(length=20), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('status_code', sa.Integer(), nullable=True),
    sa.Column('response_time', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_request_timestamp'), 'request', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_request_timestamp'), table_name='request')
    op.drop_table('request')
    # ### end Alembic commands ###
