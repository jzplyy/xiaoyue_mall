from django.contrib import admin
from django.utils.encoding import escape_uri_path
# Register your models here.
from django.http import HttpResponse
from openpyxl import Workbook

from .models import Goods

# from .models import profit_li

# 接收一个参数（模型示例）的可调用对象
g = Goods()


def sales_volume(g):
    sales = g.price * g.sales
    return "{}销售额为:{}元".format(g.name, sales)


sales_volume.short_description = '商品销售额'

from django.utils.translation import gettext_lazy as _  # 惰性翻译


class BrandListFilter(admin.SimpleListFilter):
    title = '商品名称'
    parameter_name = 'brand_name'

    def lookups(self, request, model_admin):
        return (
            ('0', _('Apple MacBook Pro')),
            ('1', _('Apple iPhone')),
            ('2', _('华为')),
            ('3', _('小米')),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(name__istartswith='Apple MacBook Pro')
        if self.value() == '1':
            return queryset.filter(name__istartswith='Apple iPhone')
        if self.value() == '2':
            return queryset.filter(name__istartswith='华为')
        if self.value() == '3':
            return queryset.filter(name__istartswith='小米')


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # 显示列表
    list_display = ('id', 'create_time', 'update_time', 'name',
                    'price', 'stock', 'sales')

    # list_display = (sales_volume,)
    # g = Goods()
    # def sales_volume(self,g):
    #     sales = g.price * g.sales
    #     return "{}销售额为:{}元".format(g.name, sales)
    # sales_volume.short_description = '商品销售额'

    # list_display = ('profit_margin',)  # 设置显示字段
    # list_display_links = ('id','name') # 设置字段链接
    list_filter = ('name',)            # 过滤器字段名称
    # list_filter = (BrandListFilter,)  # 使用自定义过滤器

    # list_per_page = 5  # 设置每页显示条数
    # list_editable = ('name',)          # 设置可编辑字段
    # search_fields = ('name',)  # 设置搜索字段

    # actions_on_top = False             # 设置管理员动作是不在顶部展示
    # actions_on_bottom = True           # 设置管理员动作是在底部展示

    # 设置action 动作

    def download_excel(self, request, queryset):
        file_name = '商品信息.xlsx'
        meta = self.model._meta  # 用于定义文件名, 格式为: app名.模型类名
        # 模型所有字段名
        field_names = [field.name for field in meta.fields]
        # 定义响应内容类型
        response = HttpResponse(content_type='application/msexcel')
        # 定义响应数据格式
        # response['Content-Disposition'] = f'attachment;filename = {meta}.xlsx'
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
        wb = Workbook()  # 新建Workbook
        ws = wb.active  # 使用当前活动的Sheet表
        ws.append(['ID', '创建时间', '更新时间', '商品名称', '价格', '库存', '销量'])  # 将模型字段名作为标题写入第一行
        for obj in queryset:  # 遍历选择的对象列表
            # obj--> id:名称   17: 小米CC9Pro 8GB+128GB 暗夜魅影
            for field in field_names:
                # 将模型属性值的文本格式组成列表
                data = [getattr(obj, field) for field in field_names]
                # 添加利润率
                # data.append(str(profit_li[int(goods_id) - 1]))
            ws.append(data)  # 写入模型属性值
        wb.save(response)  # 将数据存入响应内容
        return response

    #
    download_excel.short_description = "下载商品信息"
    actions = (download_excel,)

    """
    编辑页操作
    """
    # fields = ('name','price')
    # 设置分栏显示
    # fields = (('name', 'price'),('stock', 'sales'))

    # fieldsets = (
    #     ('商品基本信息', {'fields': ['name', 'stock', 'sales']}),
    #     ('商品价格信息', {'fields': ['price']})
    # )
    # readonly_fields = ('name',) # name字段为只读字段
    # preserver_filters = False
    # save_on_top = True