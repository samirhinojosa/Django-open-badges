from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedAuthModel
from apps.core.utils import compress_image, thumbnail_image
from .helpers import issuer_image, issuer_image_thumb


class Issuer(TimeStampedAuthModel):
    """
    Issuer's information.
    Missing fields: type, publicKey, verification, revocationList
    """
    name = models.CharField("Issuer", max_length=150, help_text="Name of the issuer")
    url = models.URLField("Website", max_length=200, blank=True, help_text="Website of the issuer")
    slug = models.SlugField("Slug", max_length=150, help_text="Name of the issuer in format URL")
    telephone = models.CharField("Telephone", max_length=50, blank=True,
                                 help_text="Telephone of the issuer")
    description = models.TextField("Description", max_length=500, blank=True,
                                   help_text="Enter a brief description of the issuer")
    image = models.ImageField("Image", max_length=250, blank=True, upload_to=issuer_image,
                              help_text="Image of the issuer")
    image_thumb = models.ImageField("Thumbnail", max_length=250, blank=True,
                                    upload_to=issuer_image_thumb, help_text="Thumbnail of the post")
    email = models.EmailField("Email", max_length=100, help_text="Email of the issuer")
    location = models.CharField("Location", max_length=150, help_text="Location of the issuer")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Issuer"
        verbose_name_plural = "Issuers"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.created:
            original = Issuer.objects.get(pk=self.pk)
            if original.image != self.image:
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)
        else:
            if self.image != "":
                self.image = compress_image(self.image)
                self.image_thumb = thumbnail_image(self.image)

        super(Issuer, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("admin:diplomas_issuer_change", args=[str(self.id)])


class Tag(TimeStampedAuthModel):
    """
    Store a simple Tag, related to Diploma
    """
    name = models.CharField("Tag", max_length=150, unique=True, help_text="Name of the tag")
    slug = models.SlugField("Slug", max_length=150, db_index=True, unique=True,
                            help_text="Name of the tag in format URL")

    class Meta:
        ordering = ["name"]
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("admin:diplomas_tag_change", args=[str(self.id)])


class Event(TimeStampedAuthModel):
    """
    Store a event
    Missing fields: type, alignment
    """
    class DiplomaType(models.TextChoices):
        CERTIFICATE = "C", _("Certificate")
        BADGE = "B", _("Badge")

    issuer = models.ForeignKey(Issuer, on_delete=models.CASCADE, help_text="Even's issuer")
    tags = models.ManyToManyField(Tag, related_name="events_tags", help_text="Tags of the event")
    name = models.CharField("Event", max_length=150, help_text="Name of the event")
    slug = models.SlugField("Slug", max_length=150, help_text="Name of the event in format URL")
    url = models.URLField("Website", max_length=200, blank=True, help_text="Website of the even")
    diploma_type = models.CharField(max_length=2, choices=DiplomaType.choices,
                                    default=DiplomaType.BADGE)
    description = models.TextField("Description", max_length=500, blank=True,
                                   help_text="Enter a brief description of the event")
    location = models.CharField("Location", max_length=150, blank=True,
                                help_text="Location of the event")

    class Meta:
        ordering = ["-created"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return "%s - %s" % (self.name, self.issuer.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("admin:diplomas_event_change", args=[str(self.id)])
