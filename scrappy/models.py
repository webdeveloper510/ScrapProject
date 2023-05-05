from django.db import models


class WebDataScraping(models.Model):
    image_url=models.TextField(max_length=1000)
    anchor=models.TextField(max_length=1000)
    title=models.TextField(max_length=1000)
