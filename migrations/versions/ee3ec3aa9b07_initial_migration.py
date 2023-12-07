"""initial migration

Revision ID: ee3ec3aa9b07
Revises: 
Create Date: 2023-12-07 01:48:06.488245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee3ec3aa9b07'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('commentID', sa.Integer(), nullable=False),
    sa.Column('postID', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('commentID')
    )
    op.create_table('hearts',
    sa.Column('heartID', sa.Integer(), nullable=False),
    sa.Column('postID', sa.Integer(), nullable=True),
    sa.Column('hearted', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('heartID')
    )
    op.create_table('posts',
    sa.Column('postID', sa.Integer(), nullable=False),
    sa.Column('caption', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('postID')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('fName', sa.String(), nullable=True),
    sa.Column('lName', sa.String(), nullable=True),
    sa.Column('pw', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    op.drop_table('hearts')
    op.drop_table('comments')
    # ### end Alembic commands ###
