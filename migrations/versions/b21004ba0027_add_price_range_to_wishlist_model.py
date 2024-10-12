"""Add price_range to Wishlist model

Revision ID: b21004ba0027
Revises: f2bf585aa1ed
Create Date: 2024-10-12 20:48:57.123456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b21004ba0027'
down_revision = 'f2bf585aa1ed'
branch_labels = None
depends_on = None


def upgrade():
    # Step 1: Add the column as nullable
    op.add_column('wishlist', sa.Column('price_range', sa.String(10), nullable=True))
    
    # Step 2: Update existing rows with a default value
    op.execute("UPDATE wishlist SET price_range = 'medium' WHERE price_range IS NULL")
    
    # Step 3: Alter the column to be non-nullable
    op.alter_column('wishlist', 'price_range', nullable=False)


def downgrade():
    op.drop_column('wishlist', 'price_range')
