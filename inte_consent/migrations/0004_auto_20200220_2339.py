# Generated by Django 2.2.9 on 2020-02-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inte_consent", "0003_auto_20200220_2308"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="identity_type",
            field=models.CharField(
                choices=[
                    ("country_id", "Country ID number"),
                    ("drivers", "Driver's license"),
                    ("passport", "Passport"),
                    ("clinic_no", "Clinic number"),
                    ("hospital_no", "Hospital number"),
                    ("mobile_no", "Mobile number"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What type of identity number is this?",
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectconsent",
            name="screening_identifier",
            field=models.CharField(
                db_index=True,
                help_text="(readonly)",
                max_length=50,
                verbose_name="Screening identifier",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="identity_type",
            field=models.CharField(
                choices=[
                    ("country_id", "Country ID number"),
                    ("drivers", "Driver's license"),
                    ("passport", "Passport"),
                    ("clinic_no", "Clinic number"),
                    ("hospital_no", "Hospital number"),
                    ("mobile_no", "Mobile number"),
                    ("OTHER", "Other"),
                ],
                max_length=25,
                verbose_name="What type of identity number is this?",
            ),
        ),
        migrations.AlterField(
            model_name="subjectconsent",
            name="screening_identifier",
            field=models.CharField(
                help_text="(readonly)",
                max_length=50,
                unique=True,
                verbose_name="Screening identifier",
            ),
        ),
    ]
