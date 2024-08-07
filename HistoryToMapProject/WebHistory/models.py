from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name_event = models.CharField(max_length=100, blank=False)
    path_img = models.BinaryField(blank=False, default=b'')
    path_img_map = models.BinaryField(blank=False, default=b'')

    def __str__(self):
        return self.name_event

class DirectionLines(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name_direction_line = models.TextField(blank=False)
    path_img_line = models.BinaryField(blank=False, default=b'')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='direction_lines')

    def __str__(self):
        return self.name_direction_line
class SideBoundaries(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
    name_side_boundaries = models.TextField(blank=False)
    path_img_boundaries = models.BinaryField(blank=False, default=b'')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='direction_boundaries')

    def __str__(self):
        return self.name_side_boundaries