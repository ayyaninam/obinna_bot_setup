from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Fee(models.Model):
    fee = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.fee >= 100:
            raise ValidationError("Fee must be less than 100")
        super(Fee, self).save(*args, **kwargs)

    def __str__(self):
        return f"Fee: {self.fee}"
    

class RoomCreation(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.title}"
    

class Channel(models.Model):
    channel_id = models.IntegerField(null=False, blank=True)
    artist = models.CharField(max_length=255, null=False, blank=False)
    influencer = models.CharField(max_length=255, null=False, blank=False)
    artist_id = models.IntegerField(blank=False, null=False)
    influencer_id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.artist}-x-{self.influencer}-{self.channel_id}"

class Task(models.Model):
    channel = models.ForeignKey(Channel, null=False, blank=False, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255, null=False, blank=False)
    artist_agreed = models.BooleanField(default=False, blank=False, null=False)
    influencer_agreed = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return f"{self.task_name}"