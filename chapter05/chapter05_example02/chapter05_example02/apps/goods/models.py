from django.db import models

# Create your models here.
class Goods(models.Model):
    """商品SKU"""
    # 可以利用null和blank属性使部分字段留空
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    name = models.CharField(max_length=50, verbose_name='名字')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    stock = models.IntegerField(default=0, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    class Meta:
        db_table = 'tb_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '%s: %s' % (self.id, self.name)

