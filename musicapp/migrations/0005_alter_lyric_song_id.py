# Generated by Django 4.1 on 2022-10-24 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0004_rename_content_lyric_lyric"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lyric",
            name="song_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="musicapp.song"
            ),
        ),
    ]