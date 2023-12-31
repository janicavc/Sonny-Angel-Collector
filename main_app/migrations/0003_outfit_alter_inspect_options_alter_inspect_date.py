# Generated by Django 4.2.3 on 2023-07-31 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_inspect'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterModelOptions(
            name='inspect',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='inspect',
            name='date',
            field=models.DateField(verbose_name='Inspect Date'),
        ),
    ]
