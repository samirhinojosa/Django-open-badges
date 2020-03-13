from django.test import TransactionTestCase
from apps.diplomas.models import Issuer, Event, Tag
from apps.diplomas.utils import create_image_issuer


MODELS = [Issuer, Event, Tag]


class IssuerTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        image = create_image_issuer(True)
        self.issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                            url="https://www.univ-montp3.fr/",
                                            email="webmaster@univ-montp3.fr",
                                            location="Montpellier, France",
                                            image=image)

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_verbose_name(self):
        self.assertEqual(str(self.issuer._meta.verbose_name), "Issuer")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.issuer._meta.verbose_name_plural), "Issuers")

    def test__str__(self):
        self.assertEqual(self.issuer.__str__(), "Université Paul-Valéry")

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
        self.assertURLEqual(self.issuer.get_absolute_url(), "/myadmin/diplomas/issuer/1/change/")


class EventTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                       url="https://www.univ-montp3.fr/",
                                       email="webmaster@univ-montp3.fr",
                                       location="Montpellier, France")
        tag = Tag.objects.create(name="Software Development")
        self.event = Event.objects.create(issuer=issuer, name="Agile Methodologies",
                                          url="https://www.univ-montp3.fr/agile-methodologies",
                                          location="Montpellier, France")
        self.event.tags.add(tag)

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_verbose_name(self):
        self.assertEqual(str(self.event._meta.verbose_name), "Event")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.event._meta.verbose_name_plural), "Events")

    def test__str__(self):
        self.assertEqual(self.event.__str__(), "Agile Methodologies - Université Paul-Valéry")

    def test_get_absolute_url(self):
        self.assertURLEqual(self.event.get_absolute_url(), "/myadmin/diplomas/event/1/change/")


class TagTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.tag = Tag.objects.create(name="Software Development")

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_verbose_name(self):
        self.assertEqual(str(self.tag._meta.verbose_name), "Tag")

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.tag._meta.verbose_name_plural), "Tags")

    def test__str__(self):
        self.assertEqual(self.tag.__str__(), "Software Development")

    def test_slug(self):
        self.assertEqual(self.tag.slug, "software-development")

    def test_get_absolute_url(self):
        self.assertURLEqual(self.tag.get_absolute_url(), "/myadmin/diplomas/tag/1/change/")
