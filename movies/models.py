from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="adı")
    description = models.TextField(verbose_name="açıklama")
    image = models.CharField(max_length=100, verbose_name="resim")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="oluşturulma tarihi")
    isPublished = models.BooleanField(default=True, verbose_name="yayınlandı mı?")
    def __str__(self):
        return self.name
    
    def get_image_path(self):
        return '/img/'+ self.image