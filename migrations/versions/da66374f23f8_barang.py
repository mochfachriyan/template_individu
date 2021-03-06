"""'barang'

Revision ID: da66374f23f8
Revises: 
Create Date: 2021-12-20 08:50:15.639950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'da66374f23f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zzz_dummy_karyawan')
    op.drop_table('zzz_dummy_salary')
    op.add_column('barang', sa.Column('status', sa.String(length=10), nullable=True))
    op.create_foreign_key(None, 'barang', 'suplier', ['id_suplier'], ['id_suplier'])
    op.drop_column('barang', 'keterangan')
    op.create_foreign_key(None, 'pembelian', 'user', ['id_user'], ['id_user'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pembelian', type_='foreignkey')
    op.add_column('barang', sa.Column('keterangan', mysql.VARCHAR(length=200), nullable=True))
    op.drop_constraint(None, 'barang', type_='foreignkey')
    op.drop_column('barang', 'status')
    op.create_table('zzz_dummy_salary',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nik', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('gaji_ke', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tanggal_gajian', sa.DATE(), nullable=True),
    sa.Column('salary', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('zzz_dummy_karyawan',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nik', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('golongan', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('tanggal_kerja', mysql.DATETIME(), nullable=True),
    sa.Column('status_aktif', mysql.VARCHAR(length=6), nullable=False),
    sa.Column('tanggal_input', mysql.DATETIME(), nullable=True),
    sa.Column('note', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
