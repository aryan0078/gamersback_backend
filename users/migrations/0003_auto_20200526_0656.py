# Generated by Django 3.0.6 on 2020-05-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200525_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerenddate', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=310)),
                ('currentseats', models.CharField(max_length=10)),
                ('avilseats', models.CharField(max_length=10)),
                ('firstprice', models.CharField(max_length=20)),
                ('secondprice', models.CharField(max_length=20)),
                ('thirdprice', models.CharField(max_length=20)),
                ('rules', models.CharField(max_length=300)),
                ('shedule', models.CharField(max_length=50)),
                ('teams', models.CharField(max_length=300)),
                ('watchnow', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teamreg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('squadname', models.CharField(max_length=20)),
                ('squadlogo', models.FileField(null=True, upload_to='images/', verbose_name='')),
                ('team1name', models.CharField(max_length=30)),
                ('team2name', models.CharField(max_length=30)),
                ('team3name', models.CharField(max_length=30)),
                ('team4name', models.CharField(max_length=30)),
                ('team1id', models.CharField(max_length=30)),
                ('team2id', models.CharField(max_length=30)),
                ('team3id', models.CharField(max_length=30)),
                ('team4id', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='usersdata',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='usersdata',
            name='name',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
