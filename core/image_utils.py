from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def process_image(
    image_field,
    max_width=1920,
    max_height=1080,
    quality=85,
):
    if not image_field:
        return

    image = Image.open(image_field)

    # Convert images with transparency or palette mode
    # to RGB before saving as JPEG.
    if image.mode in ('RGBA', 'LA', 'P'):
        image = image.convert('RGB')

    # Resize while maintaining the original aspect ratio.
    image.thumbnail(
        (max_width, max_height),
        Image.Resampling.LANCZOS,
    )

    buffer = BytesIO()

    image.save(
        buffer,
        format='JPEG',
        quality=quality,
        optimize=True,
        progressive=True,
    )

    filename = image_field.name.rsplit('.', 1)[0] + '.jpg'

    image_field.save(
        filename,
        ContentFile(buffer.getvalue()),
        save=False,
    )