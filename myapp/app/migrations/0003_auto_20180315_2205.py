# Generated by Django 2.0.1 on 2018-03-15 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180313_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.WeiBo', verbose_name='微博'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=500, verbose_name='评论内容'),
        ),
    ]