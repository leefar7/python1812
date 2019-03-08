from django.db import models

# Create your models here.

# 基础类

class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True


#轮播图
class Wheel(BaseModel):
    class Meta:
        db_table='axf_wheel'
# 导航
class Nav(BaseModel):
    class Meta:
        db_table='axf_nav'

# 每日必购
class MustBuy(BaseModel):
    class Meta:
        db_table='axf_mustbuy'
# 部分商品
class Shops(BaseModel):
    class Meta:
        db_table='axf_shop'
