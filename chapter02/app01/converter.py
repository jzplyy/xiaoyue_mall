from django.urls import register_converter


class MyConverter:
    regex = '1[3-9]\d{9}'  # 匹配规则

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


register_converter(MyConverter, 'mobile')  # 注册自定义的路由转换器
