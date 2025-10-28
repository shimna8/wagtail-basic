# Generated migration to add missing meta_description field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_homepage_options_homepage_body_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="meta_description",
            field=models.CharField(
                blank=True,
                help_text="Meta description for search engines (max 160 characters)",
                max_length=160,
            ),
        ),
    ]

