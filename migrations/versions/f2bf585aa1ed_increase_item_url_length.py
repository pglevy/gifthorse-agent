"""Increase item_url length

Revision ID: f2bf585aa1ed
Revises: 07397cf3babc
Create Date: 2024-10-12 20:44:27.338959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2bf585aa1ed'
down_revision = '07397cf3babc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.alter_column('item_url',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wishlist', schema=None) as batch_op:
        batch_op.alter_column('item_url',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###
