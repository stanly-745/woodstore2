# Generated by Django 4.0.5 on 2022-06-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_bill_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='customer_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]