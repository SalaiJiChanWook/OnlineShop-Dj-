# Generated by Django 4.2.6 on 2023-11-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_alter_electronicpd_price_alter_fashionpd_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronicpd',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='meida/Electronic'),
        ),
        migrations.AlterField(
            model_name='fashionpd',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='meida/Fashion'),
        ),
        migrations.AlterField(
            model_name='jewellerypd',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='meida/jewellery'),
        ),
    ]
