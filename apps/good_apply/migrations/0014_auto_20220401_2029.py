# Generated by Django 2.2.6 on 2022-04-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_apply', '0013_auto_20220401_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='组id')),
                ('group_name', models.CharField(max_length=20, verbose_name='组名')),
            ],
            options={
                'verbose_name': '组表',
                'verbose_name_plural': '组表',
            },
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='用户名')),
                ('org_id', models.BigIntegerField(blank=True, null=True, verbose_name='组id')),
            ],
            options={
                'verbose_name': '组成员表',
                'verbose_name_plural': '组成员表',
            },
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Groupperson',
        ),
        migrations.AlterField(
            model_name='apply',
            name='org_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='组id'),
        ),
        migrations.AlterField(
            model_name='position',
            name='org_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='组id'),
        ),
        migrations.AlterField(
            model_name='review',
            name='org_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='组id'),
        ),
        migrations.AlterField(
            model_name='secretary',
            name='org_id',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='组id'),
        ),
    ]
