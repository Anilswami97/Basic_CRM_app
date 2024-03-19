from django.utils.text import slugify
import uuid

def uni_slug_gen(first_name:str)->str:
    slug_data = slugify(first_name)
    from .models import Record

    while Record.objects.filter(uni_slug = slug_data):
        slug_data = f"{slug_data}-{str(uuid.uuid4())[:5]}"

    return slug_data