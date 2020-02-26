from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from apps.core.models import TimeStampedAuthModel
from apps.core.utils import compress_image, thumbnail_image
from .helpers import issuer_image, issuer_image_thumb

class Issuer(TimeStampedAuthModel):
    """
    Issuer's information.
    Missing fields: type, publicKey, verification, revocationList
    """
    name = models.CharField('Issuer', max_length=150, help_text='Name of the issuer')
    url = models.URLField('Website', max_length=200, blank=True, help_text='Website of the issuer')
    slug = models.SlugField('Slug', max_length=150, help_text='Name of the issuer in format URL')
    telephone = models.CharField('Telephone', max_length=50, blank=True,
                                 help_text='Telephone of the issuer')
    description = models.TextField('Description', max_length=500, blank=True,
                                   help_text='Enter a brief description of the issuer')
    image = models.ImageField('Image', max_length=250, blank=True, upload_to=issuer_image,
                              help_text='Image of the issuer')
    image_thumb = models.ImageField('Thumbnail', max_length=250, blank=True,
                                    upload_to=issuer_image_thumb, help_text='Thumbnail of the post')
    email = models.EmailField('Email', max_length=100, help_text='Email of the issuer')
    location = models.CharField('Location', max_length=150, help_text='Location of the issuer')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Issuer'
        verbose_name_plural = 'Issuers'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.created:
            orig = Issuer.objects.get(pk=self.pk)
            if orig.image != self.image:
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)
        else:
            if self.image != '':
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)

        super(Issuer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('issuer', args=[str(self.id)])
