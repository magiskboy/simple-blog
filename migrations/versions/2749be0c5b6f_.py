"""empty message

Revision ID: 2749be0c5b6f
Revises: 
Create Date: 2021-03-24 08:22:29.660872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2749be0c5b6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('hash_password', sa.String(length=60), nullable=False),
    sa.Column('verify_on_google', sa.Boolean(), nullable=True),
    sa.Column('verify_on_facebook', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('content', sa.String(length=5000), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('users')
    # ### end Alembic commands ###