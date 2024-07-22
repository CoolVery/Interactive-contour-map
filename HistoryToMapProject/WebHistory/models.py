from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name_event = models.CharField(max_length=100, blank=False)
    path_img = models.TextField(blank=False)
    path_img_map = models.TextField(blank=False, default="test")

    def __str__(self):
        return self.name_event

