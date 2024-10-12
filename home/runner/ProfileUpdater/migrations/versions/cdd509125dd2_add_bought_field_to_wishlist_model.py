"""Add bought field to Wishlist model

Revision ID: cdd509125dd2
Revises: 011d0b2c313d
Create Date: 2024-10-12 21:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdd509125dd2'
down_revision = '011d0b2c313d'
branch_labels = None
depends_on = None


def upgrade():
    # Step 1: Add the column as nullable
    op.add_column('wishlist', sa.Column('bought', sa.Boolean(), nullable=True))
    
    # Step 2: Update existing rows with a default value
    op.execute("UPDATE wishlist SET bought = FALSE WHERE bought IS NULL")
    
    # Step 3: Alter the column to be non-nullable
    op.alter_column('wishlist', 'bought', nullable=False)


def downgrade():
    op.drop_column('wishlist', 'bought')
