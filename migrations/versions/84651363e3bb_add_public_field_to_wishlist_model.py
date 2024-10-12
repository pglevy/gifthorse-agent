"""Add public field to Wishlist model

Revision ID: 84651363e3bb
Revises: b21004ba0027
Create Date: 2024-10-12 20:54:23.456789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84651363e3bb'
down_revision = 'b21004ba0027'
branch_labels = None
depends_on = None


def upgrade():
    # Step 1: Add the column as nullable
    op.add_column('wishlist', sa.Column('public', sa.Boolean(), nullable=True))
    
    # Step 2: Update existing rows with a default value
    op.execute("UPDATE wishlist SET public = FALSE WHERE public IS NULL")
    
    # Step 3: Alter the column to be non-nullable
    op.alter_column('wishlist', 'public', nullable=False)


def downgrade():
    op.drop_column('wishlist', 'public')
