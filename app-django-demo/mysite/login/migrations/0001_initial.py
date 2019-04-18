# Generated by Django 2.2 on 2019-04-17 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('admin_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('admin_passwd', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'administrator',
            },
        ),
        migrations.CreateModel(
            name='Mainpage',
            fields=[
                ('main_id', models.IntegerField(primary_key=True, serialize=False)),
                ('main_collection', models.TextField(blank=True, null=True)),
                ('main_followexpert', models.TextField(blank=True, null=True)),
                ('main_class_record', models.TextField(blank=True, null=True)),
                ('main_buy_record', models.TextField(blank=True, null=True)),
                ('main_inventory', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mainpage',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_passwd', models.CharField(max_length=20)),
                ('user_email', models.CharField(max_length=45)),
                ('user_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('user_avatar', models.CharField(blank=True, max_length=45, null=True)),
                ('user_idenity', models.IntegerField()),
                ('user_name', models.CharField(blank=True, max_length=45, null=True)),
                ('user_wechat', models.CharField(blank=True, max_length=15, null=True)),
                ('user_alipay', models.CharField(blank=True, max_length=15, null=True)),
                ('user_info', models.TextField(blank=True, null=True)),
                ('user_applyment', models.TextField(blank=True, null=True)),
                ('mainpage_main', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Mainpage')),
            ],
            options={
                'db_table': 'user',
                'unique_together': {('user_id', 'mainpage_main')},
            },
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('expert_id', models.IntegerField(primary_key=True, serialize=False)),
                ('expert_passwd', models.CharField(max_length=20)),
                ('expert_email', models.CharField(max_length=45)),
                ('expert_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('expert_avatar', models.CharField(blank=True, max_length=45, null=True)),
                ('expert_name', models.CharField(blank=True, max_length=45, null=True)),
                ('expert_wechat', models.CharField(blank=True, max_length=15, null=True)),
                ('expert_info', models.TextField(blank=True, null=True)),
                ('mainpage_main', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Mainpage')),
            ],
            options={
                'db_table': 'expert',
                'unique_together': {('expert_id', 'mainpage_main')},
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('comm_id', models.IntegerField(primary_key=True, serialize=False)),
                ('comm_type', models.IntegerField()),
                ('comm_info', models.TextField(blank=True, null=True)),
                ('comm_startprice', models.IntegerField(blank=True, null=True)),
                ('comm_sellprice', models.IntegerField(blank=True, null=True)),
                ('comm_img', models.CharField(blank=True, max_length=200, null=True)),
                ('comm_name', models.CharField(blank=True, max_length=45, null=True)),
                ('comm_con', models.IntegerField(blank=True, null=True)),
                ('user_mainpage_main', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mainpage_in_commidity', to='login.User')),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_in_commodity', to='login.User')),
            ],
            options={
                'db_table': 'commodity',
            },
        ),
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_img', models.CharField(max_length=200)),
                ('class_type', models.IntegerField(blank=True, null=True)),
                ('class_result', models.TextField(blank=True, null=True)),
                ('class_color', models.CharField(max_length=200)),
                ('class_tomb', models.CharField(max_length=200)),
                ('class_dynasty', models.CharField(max_length=200)),
                ('class_feature', models.CharField(max_length=200)),
                ('class_evaluate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('user_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_user_class', to='login.User')),
            ],
            options={
                'db_table': 'classification',
            },
        ),
        migrations.CreateModel(
            name='ExpertHasCommodity',
            fields=[
                ('expert_expert', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='expert_in_expertHasComm', serialize=False, to='login.Expert')),
                ('expert_info', models.TextField(blank=True, null=True)),
                ('expert_comment', models.TextField(blank=True, null=True)),
                ('expert_comment_time', models.DateField()),
                ('commodity_comm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Commodity')),
                ('expert_mainpage_main', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mianpage_in_expertHasComm', to='login.Expert')),
            ],
            options={
                'db_table': 'expert_has_commodity',
                'unique_together': {('expert_expert', 'expert_mainpage_main', 'commodity_comm')},
            },
        ),
        migrations.CreateModel(
            name='ExpertHasClassification',
            fields=[
                ('expert_expert', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='expert_in_expertHasClass', serialize=False, to='login.Expert')),
                ('expert_info', models.TextField(blank=True, null=True)),
                ('classification_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='login.Classification')),
                ('expert_mainpage_main', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mainpage_in_expertHasClass', to='login.Expert')),
            ],
            options={
                'db_table': 'expert_has_classification',
                'unique_together': {('expert_expert', 'expert_mainpage_main', 'classification_class')},
            },
        ),
    ]
