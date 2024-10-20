from django.db import models
from django.utils import timezone
# Create your models here.
class VTR_model(models.Model):
    # TSHIRT_NAMES = ['HRX','WROGN','PUMA','CK','']

    SHIRT = 'SH'
    PANTS = 'PA'
    GARMENT_TYPES = [
        (SHIRT, 'Shirt'),  # ('actual_value', 'human_readable_name')
        (PANTS, 'Pants'),
    ]
    
    type = models.CharField(
        max_length=2,
        choices=GARMENT_TYPES,  # Use the 'choices' attribute correctly
        default=SHIRT,
    )

    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='clothImgs/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=GARMENT_TYPES)
