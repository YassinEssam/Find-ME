# Generated by Django 5.0.4 on 2024-05-10 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0005_alter_lostperson_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostperson',
            name='address',
            field=models.CharField(blank=True, default='egypt', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lostperson',
            name='finder_name',
            field=models.CharField(default='ali', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lostperson',
            name='name',
            field=models.CharField(blank=True, default='empty', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lostperson',
            name='phone_number',
            field=models.CharField(default='empty', max_length=100, null=True),
        ),
    ]
