from django.db import models

# Create your models here.
class Karticka(models.Model):
    name = models.CharField(max_length=200, default='ftak')
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description