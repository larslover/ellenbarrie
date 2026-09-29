from io import BytesIO
from .image_utils import process_image
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=100, blank=True)
    button_url = models.CharField(max_length=300, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

      if self.image and self.pk:

        old = HeroSection.objects.get(pk=self.pk)

        if old.image != self.image:
            process_image(self.image)

      elif self.image:
        process_image(self.image)

      super().save(*args, **kwargs)


class HistoryEntry(models.Model):
    year = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='history/',
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'year']
        verbose_name = 'History Entry'
        verbose_name_plural = 'History Entries'

    def __str__(self):
        return f'{self.year} - {self.title}'

    def save(self, *args, **kwargs):

        if self.image and self.pk:

            old = HistoryEntry.objects.get(pk=self.pk)

            if old.image != self.image:
                process_image(
                    self.image,
                    max_width=1600,
                    max_height=1200,
                )

        elif self.image:
            process_image(
                self.image,
                max_width=1600,
                max_height=1200,
            )

        super().save(*args, **kwargs)

class FarmingHero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(blank=True)
    image = models.ImageField(upload_to='farming/hero/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Farming Hero'
        verbose_name_plural = 'Farming Hero'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.image and self.pk:

            old = FarmingHero.objects.get(pk=self.pk)

            if old.image != self.image:
                process_image(
                    self.image,
                    max_width=1920,
                    max_height=1080,
                )

        elif self.image:
            process_image(
                self.image,
                max_width=1920,
                max_height=1080,
            )

        super().save(*args, **kwargs)


class FarmingUpdate(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(
        upload_to='farming/updates/',
        blank=True,
        null=True,
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date', 'order']
        verbose_name = 'Farming Update'
        verbose_name_plural = 'Farming Updates'

    def __str__(self):
        return f'{self.date} - {self.title}'

    def save(self, *args, **kwargs):

        if self.image and self.pk:

            old = FarmingUpdate.objects.get(pk=self.pk)

            if old.image != self.image:
                process_image(
                    self.image,
                    max_width=1600,
                    max_height=1200,
                )

        elif self.image:
            process_image(
                self.image,
                max_width=1600,
                max_height=1200,
            )

        super().save(*args, **kwargs)

class Child(models.Model):
    name = models.CharField(max_length=100)

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    story = models.TextField()

    image = models.ImageField(
        upload_to='children/',
    )

    date_joined = models.DateField(
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Child'
        verbose_name_plural = 'Children'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if self.image and self.pk:

            old = Child.objects.get(pk=self.pk)

            if old.image != self.image:
                process_image(
                    self.image,
                    max_width=1200,
                    max_height=1200,
                )

        elif self.image:

            process_image(
                self.image,
                max_width=1200,
                max_height=1200,
            )

        super().save(*args, **kwargs)