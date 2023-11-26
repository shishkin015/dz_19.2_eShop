# Generated by Django 4.2.6 on 2023-11-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_version_options_product_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(choices=[(True, 'опубликована'), (False, 'снять с публикации')], default=False, verbose_name='признак публикации'),
        ),
    ]