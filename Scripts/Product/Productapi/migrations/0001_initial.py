# Generated by Django 4.1.3 on 2022-11-10 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Unique', models.BooleanField()),
                ('Size', models.CharField(choices=[('10', '10'), ('20', '20'), ('30', '30')], max_length=100)),
                ('Quality', models.CharField(choices=[('high', 'high'), ('low', 'low'), ('medium', 'medium')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='productImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Images')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productapi.productmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='productColourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Colour', models.CharField(choices=[('black', 'black'), ('white', 'white'), ('blue', 'blue'), ('dark', 'dark'), ('red', 'red')], max_length=100)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productapi.productmainmodel')),
            ],
        ),
    ]
