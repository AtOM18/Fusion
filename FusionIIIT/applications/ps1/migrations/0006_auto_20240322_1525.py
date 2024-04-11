# Generated by Django 3.1.5 on 2024-03-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ps1', '0005_auto_20240322_1324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indentfile',
            old_name='indent_type',
            new_name='item_type',
        ),
        migrations.AddField(
            model_name='indentfile',
            name='grade',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='stockentry',
            name='location',
            field=models.CharField(choices=[('H1', 'Vashistha Hostel'), ('H4', 'Vivekananda Hostel'), ('H3', 'AryaBhatta Hostel'), ('SR1', 'Storage Room 1'), ('SR2', 'Storage Room 2'), ('SR3', 'Storage Room 3'), ('SR4', 'Storage Room 4'), ('SR5', 'Storage Room 5')], default='SR1', max_length=100),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='department',
            field=models.CharField(default='CSE', max_length=250),
        ),
    ]