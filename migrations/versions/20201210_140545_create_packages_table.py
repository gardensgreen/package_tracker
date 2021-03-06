"""create packages table

Revision ID: 311246c6e93b
Revises: 
Create Date: 2020-12-10 14:05:45.047239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311246c6e93b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender', sa.String(length=20), nullable=False),
    sa.Column('recipient', sa.String(length=20), nullable=False),
    sa.Column('origin', sa.String(length=20), nullable=False),
    sa.Column('destination', sa.String(length=20), nullable=False),
    sa.Column('location', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages')
    # ### end Alembic commands ###
