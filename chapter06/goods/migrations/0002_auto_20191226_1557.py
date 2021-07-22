# Generated by Django 2.2.3 on 2019-12-26 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.RemoveField(
            model_name='goods',
            name='cost_price',
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=50, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='价格'),
        ),
    ]