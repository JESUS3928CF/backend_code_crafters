# Generated by Django 4.2.5 on 2023-09-28 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('code_crafters_api', '0007_educationalinstitution_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalinstitution',
            name='id_support',
        ),
        migrations.CreateModel(
            name='SupportEducationalInstitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_educationalInstitution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_crafters_api.educationalinstitution')),
                ('id_support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='code_crafters_api.support')),
            ],
        ),
    ]