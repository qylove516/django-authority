from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserInfo(AbstractUser):
    """用户表"""
    company = models.CharField('公司', max_length=64)
    address = models.CharField('联系地址', max_length=128)
    tel = models.CharField('联系电话', max_length=64)
    create_time = models.DateTimeField('创建时间', auto_now=True)
    role = models.ManyToManyField(to='Role')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Role(models.Model):
    title = models.CharField('标题', max_length=64)
    permission = models.ManyToManyField(to='Permission')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = '角色'


class Permission(models.Model):
    title = models.CharField('标题', max_length=64)
    url = models.CharField('路由', max_length=128)
    action = models.CharField('动作', max_length=32, default="")
    group = models.ForeignKey(
        to='PermissionGroup',
        on_delete=models.CASCADE,
        default=1,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = '权限'


class PermissionGroup(models.Model):
    title = models.CharField('标题', max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '权限组'
        verbose_name_plural = '权限组'
