# Generated by Django 4.0.6 on 2022-08-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_rename_senha_employees_email_rename_cpf_employees_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=50)),
                ('id_request', models.IntegerField(default=0)),
            ],
        ),
    ]
