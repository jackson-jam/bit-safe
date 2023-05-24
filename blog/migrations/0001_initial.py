# Generated by Django 4.0 on 2022-11-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appraise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('like', models.CharField(max_length=255)),
                ('appraise', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Browse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('create_time', models.CharField(max_length=255)),
                ('update_time', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=255)),
                ('cust_address', models.CharField(max_length=255)),
                ('cust_city', models.CharField(max_length=255)),
                ('cust_zip', models.CharField(max_length=255)),
                ('cust_country', models.CharField(max_length=255)),
                ('cust_contact', models.CharField(max_length=20)),
                ('cust_email', models.CharField(max_length=255)),
                ('cust_num', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=20)),
                ('order_data', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=255)),
                ('prod_price', models.CharField(max_length=255)),
                ('prod_desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('item_int', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
                ('item_price', models.CharField(max_length=255)),
                ('add_time', models.CharField(max_length=255)),
                ('item_num', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('integral', models.CharField(max_length=255)),
                ('sea_num', models.CharField(max_length=255)),
                ('coll_num', models.CharField(max_length=255)),
                ('pur_num', models.CharField(max_length=255)),
                ('buy_num', models.CharField(max_length=255)),
                ('cunsume', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=32)),
                ('user_password', models.CharField(max_length=32)),
                ('user_email', models.CharField(default='1', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vender_name', models.CharField(max_length=255)),
                ('vender_address', models.CharField(max_length=255)),
                ('vender_city', models.CharField(max_length=255)),
                ('vender_zip', models.CharField(max_length=255)),
                ('vender_country', models.CharField(max_length=255)),
            ],
        ),
    ]
