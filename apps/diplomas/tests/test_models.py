from django.test import TestCase
from apps.diplomas.models import Issuer

class IssuerTest(TestCase):

    def create_issuer(self, name='Université Paul-Valéry', url='https://www.univ-montp3.fr/',
                      email='webmaster@univ-montp3.fr', location='Montpellier, France'):
        return Issuer.objects.create(name=name, url=url, email=email, location=location)

    def test_issuer_creation(self):
        w = self.create_issuer()
        self.assertTrue(isinstance(w, Issuer))
        self.assertEqual(w.__str__(), w.name)
