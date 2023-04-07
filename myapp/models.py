from django.db import models
from PIL import Image
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
# Create your models here.



class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=1)
    img=models.ImageField(upload_to='images')
    thumbnail = ImageSpecField(source='img',processors=[ResizeToFill(200, 190)], format='JPEG',options={'quality':200})
    cdr=models.FileField(upload_to='CDRFiles')
    # cdrfile=models.FileField(upload_to='cdrfiles')


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.img.path)
        if img.height > 420 and img.weight > 236:
            output_size = (420,420)
            img.thumbnail (output_size)
            img.save(self.img.path)
    def __str__(self):
        return self.name


    @staticmethod
    def get_all_prodect():
         return Product.objects.all()