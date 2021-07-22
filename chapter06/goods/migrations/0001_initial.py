# Generated by Django 2.2.3 on 2019-11-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='进价')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'tb_goods',
            },
        ),
    ]
