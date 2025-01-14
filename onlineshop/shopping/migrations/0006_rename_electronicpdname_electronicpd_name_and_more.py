# Generated by Django 4.2.6 on 2023-11-14 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_manfashioncategory_image_manfashionsubcategory_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electronicpd',
            old_name='ElectronicPdname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='fashionpd',
            old_name='FashionPdname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='jewellerypd',
            old_name='JewelleryPdname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='electronicpd',
            name='image',
        ),
        migrations.RemoveField(
            model_name='fashionpd',
            name='image',
        ),
        migrations.RemoveField(
            model_name='jewellerypd',
            name='image',
        ),
        migrations.AlterField(
            model_name='electronicpd',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fashionpd',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='jewellerypd',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='manfashioncategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Manfashion'),
        ),
        migrations.AlterField(
            model_name='manfashioncategory',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='manfashioncategory',
            name='slag',
            field=models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='manfashionsubcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ManfashionSubCategory'),
        ),
        migrations.AlterField(
            model_name='manfashionsubcategory',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='manfashionsubcategory',
            name='slag',
            field=models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='womenfashioncategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='WomenfashionCategory'),
        ),
        migrations.AlterField(
            model_name='womenfashioncategory',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='womenfashioncategory',
            name='slag',
            field=models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True)),
        ),
        migrations.AlterField(
            model_name='womenfashionsubcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='WomenfashionSubCategory'),
        ),
        migrations.AlterField(
            model_name='womenfashionsubcategory',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='womenfashionsubcategory',
            name='slag',
            field=models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True)),
        ),
        migrations.CreateModel(
            name='Rings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Mobiles')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.jewellerypd')),
            ],
        ),
        migrations.CreateModel(
            name='Neklace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Mobiles')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.jewellerypd')),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Mobiles')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.electronicpd')),
            ],
        ),
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Laptops')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.electronicpd')),
            ],
        ),
        migrations.CreateModel(
            name='EarRings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Mobiles')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.jewellerypd')),
            ],
        ),
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('slag', models.SlugField(max_length=255, unique=models.CharField(max_length=255, null=True))),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Computers')),
                ('price', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping.electronicpd')),
            ],
        ),
    ]
