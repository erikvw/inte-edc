# Generated by Django 2.2.9 on 2020-02-20 20:08

import _socket
from django.conf import settings
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sites", "0002_alter_domain_unique"),
        ("inte_subject", "0005_auto_20200213_2055"),
    ]

    operations = [
        migrations.CreateModel(
            name="BaselineCareStatus",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "hiv",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=15,
                        verbose_name="Have you previously tested <u>positive</u> for HIV",
                    ),
                ),
                (
                    "attending_hiv_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Are you receiving care at an HIV clinic",
                    ),
                ),
                (
                    "use_hiv_clinic_nearby",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Do you attend the HIV clinic within this facility",
                    ),
                ),
                (
                    "hiv_next_appt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.date_is_future],
                        verbose_name="When is your next HIV appointment",
                    ),
                ),
                (
                    "diabetic",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=25,
                        verbose_name="Have you previously been diagnosed with <u>diabetes</u> (high blood sugar)?",
                    ),
                ),
                (
                    "hypertensive",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=25,
                        verbose_name="Have you previously been diagnosed with <u>hypertension</u> (high blood pressure)?",
                    ),
                ),
                (
                    "attending_ncd_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Are you receiving care at an NCD clinic",
                    ),
                ),
                (
                    "use_ncd_clinic_nearby",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Do you attend the NCD clinic within this facility",
                    ),
                ),
                (
                    "ncd_clinic_other",
                    models.CharField(
                        max_length=50,
                        null=True,
                        verbose_name="If not in this facility, where do you attend?",
                    ),
                ),
                (
                    "ncd_clinic_other_is_study_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Is this NCD clinic an INTE study clinic?",
                    ),
                ),
                (
                    "ncd_next_appt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.date_is_future],
                        verbose_name="When is your next NCD appointment",
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "Baseline Care Status",
                "verbose_name_plural": "Baseline Care Status",
                "abstract": False,
            },
            managers=[
                ("on_site", django.contrib.sites.managers.CurrentSiteManager()),
                ("objects", edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name="HistoricalBaselineCareStatus",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True,
                        default=django_audit_fields.models.audit_model_mixin.utcnow,
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "report_datetime",
                    models.DateTimeField(
                        default=edc_utils.date.get_utcnow,
                        help_text="If reporting today, use today's date/time, otherwise use the date/time this information was reported.",
                        validators=[
                            edc_protocol.validators.datetime_not_before_study_start,
                            edc_model.validators.date.datetime_not_future,
                        ],
                        verbose_name="Report Date",
                    ),
                ),
                (
                    "consent_model",
                    models.CharField(editable=False, max_length=50, null=True),
                ),
                (
                    "consent_version",
                    models.CharField(editable=False, max_length=10, null=True),
                ),
                (
                    "history_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "hiv",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=15,
                        verbose_name="Have you previously tested <u>positive</u> for HIV",
                    ),
                ),
                (
                    "attending_hiv_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Are you receiving care at an HIV clinic",
                    ),
                ),
                (
                    "use_hiv_clinic_nearby",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Do you attend the HIV clinic within this facility",
                    ),
                ),
                (
                    "hiv_next_appt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.date_is_future],
                        verbose_name="When is your next HIV appointment",
                    ),
                ),
                (
                    "diabetic",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=25,
                        verbose_name="Have you previously been diagnosed with <u>diabetes</u> (high blood sugar)?",
                    ),
                ),
                (
                    "hypertensive",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No"), ("unknown", "Unknown")],
                        max_length=25,
                        verbose_name="Have you previously been diagnosed with <u>hypertension</u> (high blood pressure)?",
                    ),
                ),
                (
                    "attending_ncd_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Are you receiving care at an NCD clinic",
                    ),
                ),
                (
                    "use_ncd_clinic_nearby",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Do you attend the NCD clinic within this facility",
                    ),
                ),
                (
                    "ncd_clinic_other",
                    models.CharField(
                        max_length=50,
                        null=True,
                        verbose_name="If not in this facility, where do you attend?",
                    ),
                ),
                (
                    "ncd_clinic_other_is_study_clinic",
                    models.CharField(
                        choices=[
                            ("Yes", "Yes"),
                            ("No", "No"),
                            ("N/A", "Not applicable"),
                        ],
                        default="N/A",
                        max_length=15,
                        verbose_name="Is this NCD clinic an INTE study clinic?",
                    ),
                ),
                (
                    "ncd_next_appt_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[edc_model.validators.date.date_is_future],
                        verbose_name="When is your next NCD appointment",
                    ),
                ),
                ("history_date", models.DateTimeField()),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="sites.Site",
                    ),
                ),
                (
                    "subject_visit",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="inte_subject.SubjectVisit",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Baseline Care Status",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.RemoveField(model_name="generalassessmentinitial", name="site",),
        migrations.RemoveField(
            model_name="generalassessmentinitial", name="subject_visit",
        ),
        migrations.RemoveField(
            model_name="historicalgeneralassessment", name="history_user",
        ),
        migrations.RemoveField(model_name="historicalgeneralassessment", name="site",),
        migrations.RemoveField(
            model_name="historicalgeneralassessment", name="subject_visit",
        ),
        migrations.RemoveField(
            model_name="historicalgeneralassessmentinitial", name="history_user",
        ),
        migrations.RemoveField(
            model_name="historicalgeneralassessmentinitial", name="site",
        ),
        migrations.RemoveField(
            model_name="historicalgeneralassessmentinitial", name="subject_visit",
        ),
        migrations.DeleteModel(name="GeneralAssessment",),
        migrations.DeleteModel(name="GeneralAssessmentInitial",),
        migrations.DeleteModel(name="HistoricalGeneralAssessment",),
        migrations.DeleteModel(name="HistoricalGeneralAssessmentInitial",),
        migrations.AddIndex(
            model_name="baselinecarestatus",
            index=models.Index(
                fields=["subject_visit", "site", "id"],
                name="inte_subjec_subject_0a4aa9_idx",
            ),
        ),
    ]
