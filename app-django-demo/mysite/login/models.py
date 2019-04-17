# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=20)
    admin_passwd = models.CharField(max_length=20)

    class Meta:
        #managed = False
        db_table = 'administrator'


class Classification(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_img = models.CharField(max_length=200)
    class_type = models.IntegerField(blank=True, null=True)
    class_result = models.TextField(blank=True, null=True)
    class_evaluate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    user_user = models.ForeignKey('User', models.DO_NOTHING, related_name='user_user_class')
    user_mainpage_main = models.ForeignKey('User', models.DO_NOTHING, related_name='user_mainpage_main_class' )

    class Meta:
        #managed = False
        db_table = 'classification'


class Commodity(models.Model):
    comm_id = models.IntegerField(primary_key=True)
    comm_type = models.IntegerField()
    comm_info = models.TextField(blank=True, null=True)
    comm_startprice = models.IntegerField(blank=True, null=True)
    comm_sellprice = models.IntegerField(blank=True, null=True)
    comm_img = models.CharField(max_length=200, blank=True, null=True)
    comm_name = models.CharField(max_length=45, blank=True, null=True)
    comm_con = models.IntegerField(blank=True, null=True)
    user_user = models.ForeignKey('User', models.DO_NOTHING, related_name='user_in_commodity')
    user_mainpage_main = models.ForeignKey('User', models.DO_NOTHING, related_name='mainpage_in_commidity')

    class Meta:
        #managed = False
        db_table = 'commodity'


class Expert(models.Model):
    expert_id = models.IntegerField(primary_key=True)
    expert_passwd = models.CharField(max_length=20)
    expert_email = models.CharField(max_length=45)
    expert_phone = models.CharField(max_length=15, blank=True, null=True)
    expert_avatar = models.CharField(max_length=45, blank=True, null=True)
    expert_name = models.CharField(max_length=45, blank=True, null=True)
    expert_wechat = models.CharField(max_length=15, blank=True, null=True)
    expert_info = models.TextField(blank=True, null=True)
    mainpage_main = models.ForeignKey('Mainpage', models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'expert'
        unique_together = (('expert_id', 'mainpage_main'),)


class ExpertHasClassification(models.Model):
    expert_expert = models.ForeignKey(Expert, models.DO_NOTHING, primary_key=True, related_name='expert_in_expertHasClass')
    expert_mainpage_main = models.ForeignKey(Expert, models.DO_NOTHING, related_name='mainpage_in_expertHasClass')
    classification_class = models.ForeignKey(Classification, models.DO_NOTHING)
    expert_info = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'expert_has_classification'
        unique_together = (('expert_expert', 'expert_mainpage_main', 'classification_class'),)


class ExpertHasCommodity(models.Model):
    expert_expert = models.ForeignKey(Expert, models.DO_NOTHING, primary_key=True, related_name='expert_in_expertHasComm')
    expert_mainpage_main = models.ForeignKey(Expert, models.DO_NOTHING, related_name='mianpage_in_expertHasComm')
    commodity_comm = models.ForeignKey(Commodity, models.DO_NOTHING)
    expert_info = models.TextField(blank=True, null=True)
    expert_comment = models.TextField(blank=True, null=True)
    expert_comment_time = models.DateField()

    class Meta:
        #managed = False
        db_table = 'expert_has_commodity'
        unique_together = (('expert_expert', 'expert_mainpage_main', 'commodity_comm'),)


class Mainpage(models.Model):
    main_id = models.IntegerField(primary_key=True)
    main_collection = models.TextField(blank=True, null=True)
    main_followexpert = models.TextField(blank=True, null=True)
    main_class_record = models.TextField(blank=True, null=True)
    main_buy_record = models.TextField(blank=True, null=True)
    main_inventory = models.TextField(blank=True, null=True)

    class Meta:
       # managed = False
        db_table = 'mainpage'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_passwd = models.CharField(max_length=20)
    user_email = models.CharField(max_length=45)
    user_phone = models.CharField(max_length=15, blank=True, null=True)
    user_avatar = models.CharField(max_length=45, blank=True, null=True)
    user_idenity = models.IntegerField()
    user_name = models.CharField(max_length=45, blank=True, null=True)
    user_wechat = models.CharField(max_length=15, blank=True, null=True)
    user_alipay = models.CharField(max_length=15, blank=True, null=True)
    user_info = models.TextField(blank=True, null=True)
    user_applyment = models.TextField(blank=True, null=True)
    mainpage_main = models.ForeignKey(Mainpage, models.DO_NOTHING)

    class Meta:
        #managed = False
        db_table = 'user'
        unique_together = (('user_id', 'mainpage_main'),)