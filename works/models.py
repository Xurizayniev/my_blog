from django.db import models
from ckeditor_uploader.fields import RichTextUploadingFormField


class WorksCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'work category'
        verbose_name_plural = 'works category'

class WorksModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingFormField()
    created_at = models.DateTimeField(auto_now_add=True)
    work_image = models.ImageField(upload_to='works')
    category = models.ManyToManyField(WorksCategoryModel)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'