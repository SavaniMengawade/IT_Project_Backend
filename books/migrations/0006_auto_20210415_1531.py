# Generated by Django 3.0.5 on 2021-04-15 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210415_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('userFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Users')),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
