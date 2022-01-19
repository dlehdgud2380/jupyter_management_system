# Generated by Django 4.0.1 on 2022-01-19 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='request_client_name',
            new_name='clientName',
        ),
        migrations.RenameField(
            model_name='dashboard',
            old_name='container_status',
            new_name='ctnStatus',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='container_id',
        ),
        migrations.RemoveField(
            model_name='dashboard',
            name='container_name',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='ctnIP',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='ctnId',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='ctnName',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='ctnPort',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='ctnToken',
            field=models.TextField(null=True),
        ),
    ]