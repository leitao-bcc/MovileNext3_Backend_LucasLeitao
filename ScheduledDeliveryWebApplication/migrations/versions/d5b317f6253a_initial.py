"""initial

Revision ID: d5b317f6253a
Revises: 
Create Date: 2019-03-01 21:35:16.412607

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd5b317f6253a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('country', sa.String(length=45), nullable=False),
                    sa.Column('state', sa.String(length=45), nullable=False),
                    sa.Column('city', sa.String(length=45), nullable=False),
                    sa.Column('neighborhood', sa.String(length=45),
                              nullable=False),
                    sa.Column('street_name', sa.String(length=90),
                              nullable=False),
                    sa.Column('street_number', sa.String(length=10),
                              nullable=True),
                    sa.Column('postal_code', sa.String(length=10),
                              nullable=False),
                    sa.Column('complement', sa.String(length=45),
                              nullable=True),
                    sa.Column('latitude', sa.Float(precision=9),
                              nullable=False),
                    sa.Column('longitude', sa.Float(precision=9),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('categories',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=45), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('phones',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('number', sa.String(length=10), nullable=False),
                    sa.Column('ddd', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('customers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=45), nullable=False),
                    sa.Column('tax_payer_identification_number',
                              sa.String(length=20), nullable=False),
                    sa.Column('email', sa.String(length=45), nullable=False),
                    sa.Column('phone_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('merchants',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=45), nullable=False),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('rating', sa.Float(precision=2), nullable=True),
                    sa.Column('category_id', sa.Integer(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['address_id'],
                                            ['addresses.id'], ),
                    sa.ForeignKeyConstraint(['category_id'],
                                            ['categories.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('items',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=45), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('section', sa.String(length=45), nullable=False),
                    sa.Column('merchant_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['merchant_id'],
                                            ['merchants.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('merchant_phones',
                    sa.Column('merchant_id', sa.Integer(), nullable=False),
                    sa.Column('phone_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['merchant_id'],
                                            ['merchants.id'], ),
                    sa.ForeignKeyConstraint(['phone_id'], ['phones.id'], ),
                    sa.PrimaryKeyConstraint('merchant_id', 'phone_id')
                    )
    op.create_table('office_hours',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('week_day', sa.String(length=3), nullable=False),
                    sa.Column('start_time', sa.DateTime(), nullable=False),
                    sa.Column('end_time', sa.DateTime(), nullable=False),
                    sa.Column('merchant_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['merchant_id'],
                                            ['merchants.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('orders',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('customer_id', sa.Integer(), nullable=False),
                    sa.Column('merchant_id', sa.Integer(), nullable=False),
                    sa.Column('address_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('delivery_date_time', sa.DateTime(),
                              nullable=False),
                    sa.ForeignKeyConstraint(['address_id'],
                                            ['addresses.id'], ),
                    sa.ForeignKeyConstraint(['customer_id'],
                                            ['customers.id'], ),
                    sa.ForeignKeyConstraint(['merchant_id'],
                                            ['merchants.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('order_items',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=45), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('discount', sa.Integer(), nullable=True),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('addition', sa.String(length=45), nullable=True),
                    sa.Column('observations', sa.Text(), nullable=True),
                    sa.Column('order_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    op.drop_table('office_hours')
    op.drop_table('merchant_phones')
    op.drop_table('items')
    op.drop_table('merchants')
    op.drop_table('customers')
    op.drop_table('phones')
    op.drop_table('categories')
    op.drop_table('addresses')
    # ### end Alembic commands ###
