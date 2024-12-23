# Generated by Django 4.1.6 on 2024-02-19 15:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("customerapp", "0006_remove_customer_pay"),
        ("sellapp", "0007_order_subprice"),
        ("depositapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetailerPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True, editable=False, max_length=20, null=True
                    ),
                ),
                (
                    "customerID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customerapp.customer",
                    ),
                ),
                (
                    "orderID",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sellapp.order",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
