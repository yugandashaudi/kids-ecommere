# Generated by Django 4.0.3 on 2022-05-24 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_rename_carted_data_orderiteamcustomer_carted_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercustomer',
            name='vendor_name',
        ),
        migrations.AddField(
            model_name='orderiteamcustomer',
            name='vendor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.profilevendor'),
        ),
    ]
