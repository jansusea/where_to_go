from django.db import models


# Create your models here.
class Item(models.Model):
    zlid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    score = models.FloatField()
    workingexp = models.CharField(max_length=30)
    companyname = models.CharField(max_length=100)
    companysize = models.CharField(max_length=30)
    companytype = models.CharField(max_length=15)
    jobtype = models.CharField(max_length=200)
    createdate = models.DateTimeField(blank=True, null=True)
    jobname = models.CharField(max_length=50)
    enddate = models.DateTimeField(blank=True, null=True)
    edulevel = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    salary = models.CharField(max_length=20)
    avgsalary = models.IntegerField()
    zqtime = models.DateTimeField()
    keyword = models.CharField(max_length=20, blank=True, null=True)
    industry = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'item'


class LianjiaTransaction(models.Model):
    transactiondate = models.DateTimeField()
    zqtime = models.DateTimeField()
    price = models.FloatField()
    avgprice = models.FloatField(db_column='avgPrice')  # Field name made lowercase.
    ljid = models.CharField(db_column='ljID', unique=True, max_length=25)  # Field name made lowercase.
    address = models.CharField(max_length=255)
    address1 = models.CharField(max_length=15, blank=True, null=True)
    address2 = models.CharField(max_length=15, blank=True, null=True)
    address3 = models.CharField(max_length=15, blank=True, null=True)
    address4 = models.CharField(max_length=15, blank=True, null=True)
    address5 = models.CharField(max_length=15, blank=True, null=True)
    address6 = models.CharField(max_length=15, blank=True, null=True)
    address7 = models.CharField(max_length=15, blank=True, null=True)
    address8 = models.CharField(max_length=15, blank=True, null=True)
    address9 = models.CharField(max_length=15, blank=True, null=True)
    address10 = models.CharField(max_length=15, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lianjia_transaction'


class Ziroom(models.Model):
    id = models.IntegerField(primary_key=True)
    price = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    iswhole = models.IntegerField(blank=True, null=True)
    ctime = models.DateTimeField(blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    bedroom = models.CharField(max_length=2, blank=True, null=True)
    parlor = models.CharField(max_length=2, blank=True, null=True)
    district_name = models.CharField(max_length=15, blank=True, null=True)
    bizcircle_name = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ziroom'