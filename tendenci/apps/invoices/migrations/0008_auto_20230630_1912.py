# Generated by Django 3.2.18 on 2023-06-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_invoicelineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='adjusted_cancellation_fees',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='refunds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
        ),
    ]
