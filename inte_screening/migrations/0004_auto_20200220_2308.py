# Generated by Django 2.2.9 on 2020-02-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_screening", "0003_auto_20200202_2301"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="clinic_type",
            field=models.CharField(
                choices=[("hiv_clinic", "HIV Clinic"), ("ncd_clinic", "NCD Clinic")],
                max_length=25,
                verbose_name="From which type of clinic was the patient selected",
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="clinic_type",
            field=models.CharField(
                choices=[("hiv_clinic", "HIV Clinic"), ("ncd_clinic", "NCD Clinic")],
                max_length=25,
                verbose_name="From which type of clinic was the patient selected",
            ),
        ),
    ]
