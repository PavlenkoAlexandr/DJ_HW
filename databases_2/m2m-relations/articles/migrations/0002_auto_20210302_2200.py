# Generated by Django 3.1.2 on 2021-03-02 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=80, verbose_name='Тема')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Главная')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.scope')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(through='articles.ArticleScope', to='articles.Scope'),
        ),
    ]