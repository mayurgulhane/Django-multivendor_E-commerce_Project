# Generated by Django 4.1.5 on 2023-02-03 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_color_alter_product_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.color'),
        ),
        migrations.AlterField(
            model_name='color',
            name='code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
