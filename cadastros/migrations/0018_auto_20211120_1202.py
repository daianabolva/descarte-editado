# Generated by Django 3.1.7 on 2021-11-20 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0017_auto_20211120_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doacao',
            old_name='username_id',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='doadores',
            old_name='username_id',
            new_name='username',
        ),
    ]
