"""empty message

Revision ID: 35f3c9fd5c3a
Revises: 
Create Date: 2022-06-03 21:16:29.040951

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '35f3c9fd5c3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('num_upcoming_shows', sa.Integer(), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('seeking_description', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('contact')
    op.drop_table('employer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employer',
    sa.Column('MATR', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('NOM_RAIS', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('BOI_POST', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_PREF', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_COMM', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('SECT', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('CELLU', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_PAYS', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('TELE', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('EMAIL', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('PER_CONT', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('QUA_CONT', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_PIE_IDEN', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('NUM_PIE_IDEN', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_PAYS_NATI', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('COD_SEC_ECON', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_BRA_ECON', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_CLA_ECON', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_POS_EMPL', sa.VARCHAR(), server_default=sa.text("'active'::character varying"), autoincrement=False, nullable=False),
    sa.Column('COD_LANG', sa.VARCHAR(), server_default=sa.text("'0'::character varying"), autoincrement=False, nullable=False),
    sa.Column('COMM', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('USE_NAME', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('DAT_CREAT', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('NBR_TRA_ACTI', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DER_NUM_REL_DECL', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DER_NUM_REL_PAYE', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DER_MNT_PAYE', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DER_MNT_DECL', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DER_NBR_TRA_DECL', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DUR_GLO_SUSP', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('NBR_SUSP', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('ANC_DENO', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('SIGL', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DER_TRI_DECL', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('ADRE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_POST', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_SOU_PREF', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('REG_COMM', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_NAT_JURI', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_REG_EMPL', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('COD_MOD_PAY_DER_PAYE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DAT_IND_SANTE', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('IND_SANTE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DAT_MAJ_CPT_COT', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('SSP', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('VALID', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DER_TRI_DECL_RAMA', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('DER_MNT_DECL_RAMA', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('DER_NBR_TRA_DECL_RAMA', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DER_TRI_NON_DECL', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('DER_DAT_REL_DECL', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('DER_DAT_REL_PAYE', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('COD_TYP_RELA', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DER_DAT_PAYE', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('COD_TYP_RELA_REL_DECL', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ANC_MATR', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('SOU_RECOUV', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COM_BAN_PAYE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_BANQ', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('COD_TUTE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('MATR_PAIE', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('DAT_DEB_SERV', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('DAT_IMMAT', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('DAT_NAIS', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('DAT_CRE_EMPL', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('NUM_TIN', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('DAT_EMB_PRE_TRAV', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('NBR_TRA_DECL', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('DAT_DER_MODI', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('DAT_POSI', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('MATR', name='PK_a87b6c52348684f2de9326e64d8')
    )
    op.create_table('contact',
    sa.Column('firstName', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('lastName', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('emailAddress', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phoneNumber', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('phoneNumber', name='PK_7e48813080c4f2ce7ffaca44e42')
    )
    op.drop_table('Venue')
    op.drop_table('Show')
    op.drop_table('Artist')
    # ### end Alembic commands ###
