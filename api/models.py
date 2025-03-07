from django.db import models

class Task(models.Model):
    STATUS_CHOICES = {
        "IPR": "In progress",
        "PROC": "Under processing",
        "FAL": "Failed",
        "SUCC": "Successful"
    }
    uuid = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default="IPR")
    srt_content = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to="")
