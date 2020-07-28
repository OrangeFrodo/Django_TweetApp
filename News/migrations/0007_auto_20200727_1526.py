# Generated by Django 2.2 on 2020-07-27 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_tweet_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetlike',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='News.Tweet'),
        ),
    ]
