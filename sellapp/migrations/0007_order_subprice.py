# Generated by Django 4.1.6 on 2023-06-19 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sellapp", "0006_order_discountparcent_order_vatparcent"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="subPrice",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
