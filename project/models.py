from django.db import models


class Kr(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    open = models.BigIntegerField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    high = models.BigIntegerField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.BigIntegerField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    close = models.BigIntegerField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    change = models.FloatField(db_column='Change', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kr'

class Clusteringkr(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    label = models.BigIntegerField(blank=True, null=True)
    trading_value = models.BigIntegerField(db_column='Trading Value', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'clusteringkr'

class ClusteringkrInfo(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True, null=True)
    구분 = models.TextField(blank=True, null=True)
    구분상세 = models.TextField(blank=True, null=True)
    기초지수 = models.TextField(blank=True, null=True)
    설명 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clusteringkr_info'


class Krchartdata(models.Model):
    index = models.BigIntegerField(blank=True, null=False, primary_key=True)
    x0 = models.TextField(blank=True, null=True)
    x1 = models.TextField(blank=True, null=True)
    x2 = models.TextField(blank=True, null=True)
    x3 = models.TextField(blank=True, null=True)
    x4 = models.TextField(blank=True, null=True)
    x5 = models.TextField(blank=True, null=True)
    x6 = models.TextField(blank=True, null=True)
    x7 = models.TextField(blank=True, null=True)
    x8 = models.TextField(blank=True, null=True)
    x9 = models.TextField(blank=True, null=True)
    x10 = models.TextField(blank=True, null=True)
    x11 = models.TextField(blank=True, null=True)
    x12 = models.TextField(blank=True, null=True)
    x13 = models.TextField(blank=True, null=True)
    x14 = models.TextField(blank=True, null=True)
    x15 = models.TextField(blank=True, null=True)
    x16 = models.TextField(blank=True, null=True)
    x17 = models.TextField(blank=True, null=True)
    x18 = models.TextField(blank=True, null=True)
    x19 = models.TextField(blank=True, null=True)
    x20 = models.TextField(blank=True, null=True)
    x21 = models.TextField(blank=True, null=True)
    x22 = models.TextField(blank=True, null=True)
    x23 = models.TextField(blank=True, null=True)
    x24 = models.TextField(blank=True, null=True)
    x25 = models.TextField(blank=True, null=True)
    x26 = models.TextField(blank=True, null=True)
    x27 = models.TextField(blank=True, null=True)
    x28 = models.TextField(blank=True, null=True)
    x29 = models.TextField(blank=True, null=True)
    x30 = models.TextField(blank=True, null=True)
    x31 = models.TextField(blank=True, null=True)
    x32 = models.TextField(blank=True, null=True)
    x33 = models.TextField(blank=True, null=True)
    x34 = models.TextField(blank=True, null=True)
    x35 = models.TextField(blank=True, null=True)
    x36 = models.TextField(blank=True, null=True)
    x37 = models.TextField(blank=True, null=True)
    x38 = models.TextField(blank=True, null=True)
    x39 = models.TextField(blank=True, null=True)
    x40 = models.TextField(blank=True, null=True)
    x41 = models.TextField(blank=True, null=True)
    x42 = models.TextField(blank=True, null=True)
    x43 = models.TextField(blank=True, null=True)
    x44 = models.TextField(blank=True, null=True)
    x45 = models.TextField(blank=True, null=True)
    x46 = models.TextField(blank=True, null=True)
    x47 = models.TextField(blank=True, null=True)
    x48 = models.TextField(blank=True, null=True)
    x49 = models.TextField(blank=True, null=True)
    x50 = models.TextField(blank=True, null=True)
    x51 = models.TextField(blank=True, null=True)
    x52 = models.TextField(blank=True, null=True)
    x53 = models.TextField(blank=True, null=True)
    x54 = models.TextField(blank=True, null=True)
    x55 = models.TextField(blank=True, null=True)
    x56 = models.TextField(blank=True, null=True)
    x57 = models.TextField(blank=True, null=True)
    x58 = models.TextField(blank=True, null=True)
    x59 = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'krchartdata'