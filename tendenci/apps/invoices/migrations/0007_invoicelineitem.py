# Generated by Django 3.2.18 on 2023-03-15 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0006_auto_20200902_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
            ],
        ),
    ]
