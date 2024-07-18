# Generated by Django 5.0.6 on 2024-07-10 10:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                ("slug", models.SlugField(blank=True, max_length=120, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                ("level", models.IntegerField(default=0)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="inventory.category",
                    ),
                ),
            ],
        ),
        migrations.RunSQL("""
            ALTER TABLE inventory_category
            ADD CONSTRAINT inventory_category_chk_empty_name
            CHECK (name <> '' AND name is NOT NULL)  
        """),
        migrations.RunSQL("""
            CREATE OR REPLACE FUNCTION lowercase_name_trigger()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.name := LOWER(NEW.name);
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;
            
            CREATE TRIGGER category_lowercase_name_trigger
            BEFORE INSERT OR UPDATE ON inventory_category
            FOR EACH ROW
            EXECUTE FUNCTION lowercase_name_trigger();
        """),
        migrations.RunSQL("""
            ALTER TABLE inventory_category
            ADD CONSTRAINT inventory_category_chk_slug_format
            CHECK (slug ~ '^[a-z0-9_-]+$');
        """),
        migrations.RunSQL("""
            ALTER TABLE inventory_category
            ADD CONSTRAINT inventory_category_chk_unique_name_level
            UNIQUE (name, level);
        """),
        migrations.RunSQL("""
            ALTER TABLE inventory_category
            ADD CONSTRAINT inventory_category_chk_level_range
            CHECK (level >= 0 AND level <= 10);
        """),
    ]