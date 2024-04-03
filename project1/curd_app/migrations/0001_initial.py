# Generated by Django 5.0.3 on 2024-04-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CJC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_first_name', models.CharField(max_length=20)),
                ('stu_last_name', models.CharField(max_length=20)),
                ('stu_qualification', models.CharField(max_length=20)),
                ('course', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C', 'C'), ('C+', 'C+')], max_length=20)),
                ('stu_address', models.CharField(max_length=20)),
            ],
        ),
    ]