# Generated by Django 3.2.16 on 2023-03-31 15:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=20, verbose_name='아이디')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='이메일')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='닉네임')),
                ('class_of', models.IntegerField(verbose_name='입학연도')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('join_date', models.DateField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.school')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
