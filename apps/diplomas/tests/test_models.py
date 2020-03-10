from io import BytesIO
from PIL import Image
from django.core.files import File
from django.test import TestCase
from apps.diplomas.models import Issuer


def create_image_issuer(flag=False):
    """
    Create and update an image for test this attribute in the model
    """
    if flag:
        width, height = 525, 225
        color = "white"
    else:
        width, height = 1050, 550
        color = "red"

    image = Image.new("RGB", (width, height), color=color)
    im_io = BytesIO()
    image.save(im_io, format="PNG", quality=100)

    if flag:
        image = File(im_io, name=".jpg")
    else:
        image = File(im_io, name=".png")

    return image


class IssuerTest(TestCase):

    def setUp(self):
        image = create_image_issuer(True)
        self.issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                            url="https://www.univ-montp3.fr/",
                                            email="webmaster@univ-montp3.fr",
                                            location="Montpellier, France",
                                            image=image)

    def tearDown(self):
        self.issuer.delete()

    def test__str__(self):
        self.assertEqual(self.issuer.__str__(), "Université Paul-Valéry")

    def test_verbose_name(self):
        self.assertEqual(str(self.issuer._meta.verbose_name), "Issuer")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.issuer._meta.verbose_name_plural), "Issuers")

    def test_slug(self):
        self.assertEqual(self.issuer.slug, "universite-paul-valery")

    def test_image_url(self):
        self.assertURLEqual((self.issuer.image.url).split("/media/")[-1],
                            "diplomas/issuers/universite-paul-valery.jpg")

    def test_update_image(self):
        original = Issuer.objects.get(name="Université Paul-Valéry")
        original_image = original.image
        self.issuer.image = create_image_issuer()
        self.issuer.save()
        self.issuer.refresh_from_db()
        self.assertNotEqual(self.issuer.image.url, original_image.url)

    def test_get_absolute_url(self):
        self.assertURLEqual(self.issuer.get_absolute_url(), "/myadmin/diplomas/issuer/2/change/")
        