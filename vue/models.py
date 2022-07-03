from django.db import models

# Create your models here.

# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models



class Book(models.Model):
    bookName = models.CharField(max_length=128, verbose_name='书名')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.bookName

    def __str__(self):
        return self.bookName

    # class Meta:
    #     db_table = 'backend_book'

