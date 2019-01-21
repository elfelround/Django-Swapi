# Generated by Django 2.1.5 on 2019-01-20 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='propertyimage',
            name='property',
        ),
        migrations.DeleteModel(
            name='PropertyImage',
        ),
        migrations.AddField(
            model_name='people',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='starwarsapp.PeopleImage'),
        ),
    ]
