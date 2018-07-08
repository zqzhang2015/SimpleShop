# Generated by Django 2.0.6 on 2018-07-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleShop', '0005_auto_20180706_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='client_email',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='text_body',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='add_comments',
            field=models.TextField(default='comment', max_length=1000, verbose_name='Additional Comments'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='body',
            field=models.TextField(default='body', max_length=1000, verbose_name='Email Body'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='recipient_email',
            field=models.EmailField(default='email@email.com', max_length=254, verbose_name='Recipient Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(default='subject', max_length=200, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]