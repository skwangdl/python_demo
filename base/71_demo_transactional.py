from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db import transaction  # 导入事务


# 类视图 (事务,@transaction.atomic装饰器)
class MyView(View):
    @transaction.atomic
    # transaction.atomic装饰器可以保证该函数中所有的数据库操作都在一个事务中。
    def post(self, request):
        # 数据库操作1。。。
        # 数据库操作2。。。

        return HttpResponse('ok')


# 类视图 (事务,保存点的使用)
class MyView2(View):
    @transaction.atomic
    def post(self, request):
        # 设置事务保存点
        s1 = transaction.savepoint()  # 可以设置多个保存点

        # 数据库操作。。。

        # 事务回滚 (如果发生异常,就回滚事务)
        transaction.savepoint_rollback(s1)  # 可以回滚到指定的保存点

        # 提交事务 (如果没有异常,就提交事务)
        transaction.savepoint_commit(s1)

        # 返回应答
        return HttpResponse('ok')
