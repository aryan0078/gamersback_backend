# Generated by Django 3.0.6 on 2020-06-01 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200528_0402'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamreg',
            name='emailid',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='notifphone',
            field=models.CharField(default=False, max_length=12),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='phone',
            field=models.CharField(default=False, max_length=12),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='team5id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='team5name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='team6id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='teamreg',
            name='team6name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='aboutevents',
            name='eventid',
            field=models.CharField(default=False, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='fullname',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='squadname',
            field=models.CharField(default=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team1id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team2id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team3id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team3name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team4id',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='teamreg',
            name='team4name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='usersdata',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='usersdata',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
