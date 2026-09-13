from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return self.username