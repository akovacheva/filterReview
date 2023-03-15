from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.IntegerField(primary_key=True)
    reviewId = models.CharField(max_length=32)
    reviewFullText = models.CharField(max_length=100)
    reviewText = models.CharField(max_length=100)
    numLikes = models.IntegerField()
    numComments = models.IntegerField()
    numShares = models.IntegerField()
    rating = models.IntegerField()
    reviewCreatedOn = models.CharField(max_length=20)
    reviewCreatedOnDate = models.DateTimeField()
    reviewCreatedOnTime = models.IntegerField()
    reviewerId = models.IntegerField(null=True)
    reviewerUrl = models.URLField(null=True)
    reviewerName = models.CharField(max_length=50)
    reviewerEmail = models.EmailField(null=True)
    sourceType = models.CharField(max_length=20)
    isVerified = models.BooleanField()
    source = models.CharField(max_length=20)
    sourceName = models.CharField(max_length=50)
    sourceId = models.CharField(max_length=32)
    tags = models.JSONField()
    href = models.URLField(null=True)
    logoHref = models.URLField(null=True)
    photos = models.JSONField()