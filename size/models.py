from django.db import models

class Produt_size(models.Model):
    size = models.CharField(max_length=4, unique=True)

    def save(self, *args, **kwargs):
        # Convert the 'size' field value to uppercase before saving
        self.size = self.size.upper()
        super(Produt_size, self).save(*args, **kwargs)

    def __str__(self):
        return self.size
