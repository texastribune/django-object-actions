"""
Integration tests
"""
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse  # < DJANGO1.10

from .tests import LoggedInTestCase


class ChangeListTests(LoggedInTestCase):
    def test_changelist_action_is_rendered(self):
        response = self.client.get(reverse("admin:polls_choice_changelist"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'href="/admin/polls/choice/actions/delete_all/"', response.content
        )
