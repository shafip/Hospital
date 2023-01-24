# Generated by Django 4.1.5 on 2023-01-24 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('de_name', models.CharField(max_length=30)),
                ('de_description', models.CharField(max_length=300)),
                ('do_name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorIn',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.department')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('Token_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Fullname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=11)),
                ('Age', models.CharField(max_length=2)),
                ('Department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.department')),
                ('Doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinic.doctorin')),
            ],
        ),
    ]
