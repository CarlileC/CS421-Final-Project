"""empty message

Revision ID: 6164eb94cec5
Revises: 
Create Date: 2024-08-01 16:20:30.406690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6164eb94cec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Comments', sa.Column('coffee_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Comments', 'Coffee', ['coffee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Comments', type_='foreignkey')
    op.drop_column('Comments', 'coffee_id')
    # ### end Alembic commands ###
