# Generated by Django 3.1.2 on 2021-10-27 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0052_auto_20211027_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='summoner',
            options={},
        ),
        migrations.CreateModel(
            name='ChampionSummoners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platformid', models.TextField()),
                ('tier', models.TextField()),
                ('winrate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('championid', models.ForeignKey(db_column='championid', on_delete=django.db.models.deletion.PROTECT, to='api.champions', to_field='key')),
                ('summonername', models.ForeignKey(db_column='summonername', on_delete=django.db.models.deletion.PROTECT, to='api.summoner', to_field='name')),
            ],
            options={
                'db_table': 'summoner_champions',
            },
        ),
    ]