# Generated by Django 4.0.4 on 2022-05-23 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bench', '0002_alter_employee_date_of_joining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_of_joining',
            field=models.CharField(max_length=50, null=True),
        ),
    ]