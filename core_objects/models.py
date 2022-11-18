from django.db import models
from django.forms.widgets import Textarea
from sorl.thumbnail import get_thumbnail
from django.utils.safestring import mark_safe
from django.core.validators import *
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db.models.signals import post_save
from django.dispatch import receiver

def clean_picture(image):
    w, h = get_image_dimensions(image)
    if not((w /h > 1.77 and w /h < 1.78) or (w /h > 0.56 and w /h < 0.57)):
        raise ValidationError('The image ratio should be either 16:9 or 9:16')
    else:
        return image

class Slideshow(models.Model):
    year = models.IntegerField(
        'Year',
        null=True,
        blank=False,
        validators=[MinValueValidator(1800, message='Please enter a year between 1850 and 2100'),
                    MaxValueValidator(2100, message='Please enter a year between 1850 and 2100')],)   

    previewPicture=models.ImageField( 
        'Slideshow Picture',
        null=True,
        blank=False,
        validators = [clean_picture])                        

    def __str__(self):
        return str(self.year) 

    def get_thumbnail_url(self, geometry_string='x200'):
        try:
            thumbUrl = get_thumbnail( self.previewPicture, geometry_string, crop='center', quality=70).url
            linkUrl = self.previewPicture.url
        except:
            thumbUrl = ""
            linkUrl = ""
        return mark_safe('<a href="{}" style="display: block;"><img style="display: inline-block;" src="{}" /></a>'.format(linkUrl, thumbUrl))    

class SlideshowItem(models.Model):
    parent = models.ForeignKey(
        'Slideshow', 
        on_delete=models.CASCADE, 
        null=False)

    headline = models.CharField(
        'Headline',
        null=True, 
        blank=False, 
        max_length=40)
    
    bodyText= models.TextField(
        "Text" ,
        max_length = 450, 
        null = False, 
        blank = False, 
        default="",) 

    order = models.PositiveIntegerField(
        default=0,  
        null=False,
        blank=False,)
    
    image=models.ImageField( 
        'image',
        null=False,
        blank=False,
        validators = [clean_picture])

    video = models.FileField(
        upload_to='Video',
        null='True',
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])   
    
    mediaType = models.CharField(
        'mediaType',
        max_length=20,
        blank=True,
    )

    class Meta(object):
        ordering = ['order']
        
    def __str__(self):
        return str(self.pk) 

    def get_thumbnail_url(self, geometry_string='x200'):
        try:
            thumbUrl = get_thumbnail( self.image, geometry_string, crop='center', quality=70).url
            linkUrl = self.image.url
        except:
            thumbUrl = ""
            linkUrl = ""
        return mark_safe('<a href="{}" style="display: block;"><img style="display: inline-block;" src="{}" /></a>'.format(linkUrl, thumbUrl))

@receiver(post_save, sender=SlideshowItem, dispatch_uid="update_stock_count")
def update_stock(sender, instance, created, **kwargs):
    if sender.video.field.blank=="True":
        instance.mediaType = 'image'
    else:
        instance.mediaType = 'video'