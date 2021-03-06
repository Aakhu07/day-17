# Generated by Django 3.2.2 on 2021-05-17 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=400)),
                ('slug', models.CharField(max_length=400)),
                ('quantity', models.IntegerField(default=1)),
                ('total', models.IntegerField()),
                ('checkout', models.BooleanField(default=False)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.item')),
            ],
        ),
    ]
