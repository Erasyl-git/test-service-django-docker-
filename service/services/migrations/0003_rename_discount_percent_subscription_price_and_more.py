# Generated by Django 5.0.1 on 2024-04-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_subscription_discount_percent_alter_plan_plan_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='discount_percent',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan_type',
            field=models.CharField(choices=[('full', 'Full'), ('student', 'Student'), ('discount', 'Discount')], max_length=50),
        ),
    ]