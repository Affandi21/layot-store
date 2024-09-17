import uuid  # tambahkan baris ini di paling atas
from django.db import models

class LayotStore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    description = models.TextField()
    total = models.IntegerField()
   
    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5