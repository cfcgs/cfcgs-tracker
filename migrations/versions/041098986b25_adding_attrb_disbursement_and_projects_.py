"""adding attrb disbursement and projects_approved

Revision ID: 041098986b25
Revises: 9ed181776bdf
Create Date: 2025-05-21 00:02:11.159408

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '041098986b25'
down_revision: Union[str, None] = '9ed181776bdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('funds', sa.Column('disbursement', sa.Float(), nullable=True))
    op.add_column('funds', sa.Column('projects_approved', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('funds', 'projects_approved')
    op.drop_column('funds', 'disbursement')
    # ### end Alembic commands ###
