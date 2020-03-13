from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from apps.core.models import User
from apps.diplomas.models import Issuer, Tag, Event
from apps.diplomas.admins.issuers import IssuerAdmin
from apps.diplomas.admins.tags import TagAdmin
from apps.diplomas.admins.events import EventAdmin
from apps.diplomas.utils import create_image_issuer


MODELS = [Issuer, Tag, Event]


class MockRequest(object):
    def __init__(self, user=None):
        self.user = user


class AdminIssuerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="sam",
                                             email="sam@gmail.com",
                                             password="sam_pwd")

        self.issuer = Issuer(name="Université Paul-Valéry",
                             url="https://www.univ-montp3.fr/",
                             email="webmaster@univ-montp3.fr",
                             location="Montpellier, France")
        self.issuer_admin = IssuerAdmin(model=Issuer, admin_site=AdminSite())
        self.issuer_admin.save_model(obj=self.issuer, request=MockRequest(user=self.user),
                                     form=None, change=False)

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_thumbnail_no_image(self):
        self.assertEqual(self.issuer_admin.thumbnail(self.issuer),
                         '<img src="/static/not-available.png" width="75" height="75" >')

    def test_thumbnail_image(self):
        self.issuer.image = create_image_issuer(True)
        self.issuer.save()
        self.assertEqual(self.issuer_admin.thumbnail(self.issuer),
                         '<img src="/media/diplomas/issuers/thumbnails' +
                         '/universite-paul-valery_thumb.jpg"' +
                         ' width="75" height="auto" >')

    def test_save_model(self):
        self.assertEqual(self.issuer.modified_by, None)
        self.issuer.name = "Université Paul-Valéry de France"
        self.issuer_admin.save_model(obj=self.issuer, request=MockRequest(user=self.user),
                                     form=None, change=True)
        self.assertEqual(self.issuer.modified_by.username, "sam")


class AdminTagTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="sam",
                                             email="sam@gmail.com",
                                             password="sam_pwd")

        self.tag = Tag(name="Agile Development")
        self.tag_admin = TagAdmin(model=Tag, admin_site=AdminSite())
        self.tag_admin.save_model(obj=self.tag, request=MockRequest(user=self.user),
                                  form=None, change=False)

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_save_model(self):
        self.assertEqual(self.tag.modified_by, None)
        self.tag.name = "Agile Development Scrum"
        self.tag_admin.save_model(obj=self.tag, request=MockRequest(user=self.user),
                                  form=None, change=True)
        self.assertEqual(self.tag.modified_by.username, "sam")


class AdminEventTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="sam",
                                             email="sam@gmail.com",
                                             password="sam_pwd")

        issuer = Issuer.objects.create(name="Université Paul-Valéry",
                                       url="https://www.univ-montp3.fr/",
                                       email="webmaster@univ-montp3.fr",
                                       location="Montpellier, France")
        tag = Tag.objects.create(name="Software Development")

        self.event = Event(issuer=issuer, name="Bootcamp Agile",
                           url="http://www.bootcamp-agile.com", diploma_type="B",
                           location="Montpellier, France")
        self.event_admin = EventAdmin(model=Event, admin_site=AdminSite())
        self.event_admin.save_model(obj=self.event, request=MockRequest(user=self.user),
                                    form=None, change=False)
        self.event.tags.add(tag.id)

    def tearDown(self):
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()

    def test_save_model(self):
        self.assertEqual(self.event.modified_by, None)
        self.event.name = "Bootcamp Agile Scrum"
        self.event_admin.save_model(obj=self.event, request=MockRequest(user=self.user),
                                    form=None, change=True)
        self.assertEqual(self.event.modified_by.username, "sam")
