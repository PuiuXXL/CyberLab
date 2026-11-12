"""Add category and description to labs.

Revision ID: e2d91fc05a7b
Revises: c4fe22907839
"""

from alembic import op
import sqlalchemy as sa


revision = "e2d91fc05a7b"
down_revision = "c4fe22907839"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("labs", sa.Column("category", sa.String(100), nullable=True))
    op.add_column("labs", sa.Column("description", sa.Text(), nullable=True))

    labs = sa.table(
        "labs",
        sa.column("image", sa.String()),
        sa.column("category", sa.String()),
        sa.column("description", sa.Text()),
    )
    metadata = (
        (
            "cyberlab/sql-injection:demo",
            "Baze de date",
            "Vezi cum o intrare neverificată poate modifica o interogare SQL.",
        ),
        (
            "cyberlab/xss:demo",
            "Securitatea browserului",
            "Înțelege cum ajunge un script injectat să ruleze în browser.",
        ),
        (
            "cyberlab/access-control:demo",
            "Controlul accesului",
            "Explorează ce se întâmplă când aplicația nu verifică permisiunile.",
        ),
    )
    for image, category, description in metadata:
        op.execute(
            labs.update()
            .where(labs.c.image == op.inline_literal(image))
            .values(
                category=op.inline_literal(category),
                description=op.inline_literal(description),
            )
        )


def downgrade() -> None:
    op.drop_column("labs", "description")
    op.drop_column("labs", "category")
