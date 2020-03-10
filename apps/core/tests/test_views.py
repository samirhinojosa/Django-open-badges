from django.test import TestCase, RequestFactory
from apps.core.views import IndexRedirectView


class IndexRedirectViewTest(TestCase):

    def test_get(self):
        request_factory = RequestFactory()
        self.assertURLEqual(IndexRedirectView.get(self, request_factory),
                            '<HttpResponseRedirect status_code=302, ' +
                            '"text/html; charset=utf-8", url="myadmin/">')
