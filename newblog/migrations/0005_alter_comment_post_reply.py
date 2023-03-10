# Generated by Django 4.1.5 on 2023-01-31 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newblog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='newblog.blognew'),
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='newblog.blognew')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newblog.comment')),
            ],
        ),
    ]
