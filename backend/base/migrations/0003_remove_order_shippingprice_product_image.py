# Generated by Django 4.0.6 on 2022-07-27 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_order_review_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shippingPrice',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
