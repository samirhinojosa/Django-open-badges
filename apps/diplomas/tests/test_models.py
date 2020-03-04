from io import BytesIO
from PIL import Image
from django.core.files import File
from django.test import TestCase
from apps.diplomas.models import Issuer


def create_image_issuer():
    """
    Create an image for test this attribute in the model
    """
    width, height = 525, 225

    img_badge_in = Image.new("RGB", (width, height), color="white")

    im_io = BytesIO()
    img_badge_in.save(im_io, format="PNG", quality=100)
    img_badge_in = File(im_io, name=".jpg")

    return img_badge_in


class IssuerTest(TestCase):

    def setUp(self):
        image = create_image_issuer()
        self.issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                            url="https://www.univ-montp3.fr/",
                                            email="webmaster@univ-montp3.fr",
                                            location="Montpellier, France",
                                            image=image)

    def tearDown(self):
        self.issuer.delete()

    def test_verbose_name(self):
        self.assertEqual(str(self.issuer._meta.verbose_name), "Issuer")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.issuer._meta.verbose_name_plural), "Issuers")

    def test_slug(self):
        self.assertEqual(self.issuer.slug, "universite-paul-valery")

    def test_image_url(self):
        self.assertEqual((self.issuer.image.url).split("/media/")[-1],
                         "diplomas/issuers/universite-paul-valery.jpg")

    def test_get_absolute_url(self):
        self.assertEqual(self.issuer.get_absolute_url(), "/myadmin/diplomas/issuer/1/change/")
        