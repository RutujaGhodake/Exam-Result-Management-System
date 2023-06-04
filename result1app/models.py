from django.db import models

class stdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.BigIntegerField()
    marathi=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    math=models.IntegerField()
    science=models.IntegerField()
    ssci=models.IntegerField()

class hscdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    english=models.IntegerField()
    marathi=models.IntegerField()
    math=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    biology=models.IntegerField()


class degreedata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    bcomm=models.IntegerField()
    pm=models.IntegerField()
    c=models.IntegerField()
    dbms=models.IntegerField()
    stat=models.IntegerField()

class degree2data(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    htno = models.IntegerField()
    dm = models.IntegerField()
    ds = models.IntegerField()
    se = models.IntegerField()
    php = models.IntegerField()
    bd = models.IntegerField()

class degree3data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    st=models.IntegerField()
    rit=models.IntegerField()
    java=models.IntegerField()
    android=models.IntegerField()
    project=models.IntegerField()

class btechdata(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    eng=models.IntegerField()
    ap=models.IntegerField()
    math=models.IntegerField()
    cit=models.IntegerField()
    sdc=models.IntegerField()
    cds=models.IntegerField()

class btech2data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    co=models.IntegerField()
    itm=models.IntegerField()
    et=models.IntegerField()
    dc=models.IntegerField()
    ps=models.IntegerField()
    opr=models.IntegerField()

class btech3data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    ca=models.IntegerField()
    ai=models.IntegerField()
    nf=models.IntegerField()
    wn=models.IntegerField()
    dsa=models.IntegerField()
    ipl=models.IntegerField()

class btech4data(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    htno=models.IntegerField()
    se=models.IntegerField()
    sm=models.IntegerField()
    java=models.IntegerField()
    mc=models.IntegerField()
    ds=models.IntegerField()
    pr=models.IntegerField()

