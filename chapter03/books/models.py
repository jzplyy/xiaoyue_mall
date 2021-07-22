from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name="名称")
    pub_date = models.DateField(verbose_name="发布日期")
    readcount = models.IntegerField(default=0, verbose_name="阅读量")
    commentcount = models.IntegerField(default=0, verbose_name="评论量")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")

    def __str__(self):
        return self.name

    # 定义元属性
    class Meta:
        db_table = 'tb_bookinfo'


# 自定义管理器
# 自定义管理器
class CountryManager(models.Manager):
    def country_name_prefix(self):
        # 查询所有结果
        all_countries = self.all()
        for country in all_countries:
            country.country_name = '国家：' + country.country_name
        return all_countries


# 一对多
class Country(models.Model):
    country_code = models.CharField(max_length=20)
    country_name = models.CharField(max_length=50)

    objects = CountryManager()

    class Meta:
        db_table = 'country'

    def __str__(self):
        return self.country_name


class PersonManager(models.Manager):
    def get_queryset(self):
        return super(PersonManager, self).get_queryset().filter(person_nation__exact=1)


class Person(models.Model):
    person_name = models.CharField(max_length=20)
    person_age = models.IntegerField(default=0)
    person_money = models.IntegerField(default=0)
    person_nation = models.ForeignKey(Country, on_delete=models.CASCADE)

    objects = PersonManager()


class Meta:
    db_table = "person"


# 一对一
class President(models.Model):
    president_name = models.CharField(max_length=20)
    president_gender = models.CharField(max_length=10)
    president_nation = models.OneToOneField(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = "president"


# 多对多
class Teachers(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = "teachers"


class Students(models.Model):
    name = models.CharField(max_length=10)
    classes = models.ManyToManyField(Teachers)

    class Meta:
        db_table = "students"
