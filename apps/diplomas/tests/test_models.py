from django.conf import settings
from django.test import TestCase
from apps.diplomas.models import Issuer

""" https://swapps.com/blog/testing-files-with-pythondjango/
https://dirtycoder.net/2016/02/09/testing-a-model-that-have-an-imagefield/ """


class IssuerTest(TestCase):

    def setUp(self):
        self.issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                            url="https://www.univ-montp3.fr/",
                                            email="webmaster@univ-montp3.fr",
                                            location="Montpellier, France")

    def tearDown(self):
        self.issuer.delete()

    def test_verbose_name(self):
        self.assertEqual(str(self.issuer._meta.verbose_name), "Issuer")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.issuer._meta.verbose_name_plural), "Issuers")

    """ def test_image_url(self):
        self.assertEqual(self.issuer.image_url, "/temp/universite-paul-valery.jpeg") """

    def test_get_absolute_url(self):
        self.assertEqual(self.issuer.get_absolute_url(), "/myadmin/diplomas/issuer/1/change/")
        