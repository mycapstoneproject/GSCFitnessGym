# Generated by Django 4.2 on 2024-10-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0007_member_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='pricing',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
