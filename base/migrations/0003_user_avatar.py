# Generated by Django 4.1.3 on 2022-11-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_bio_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]
