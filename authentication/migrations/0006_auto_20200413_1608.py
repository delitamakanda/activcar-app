# Generated by Django 2.2.10 on 2020-04-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20200308_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Faculty'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Job'),
        ),
        migrations.AlterField(
            model_name='student',
            name='cursus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Cursus'),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.Faculty'),
        ),
    ]