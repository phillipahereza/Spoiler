from django.test import TestCase

from spoiler.tv_spoiler.models import Victim


class TestVictimModel(TestCase):
    def test_string_representation(self):
        victim = Victim(name='Ahereza', telephone_number='+256782000000')
        self.assertEqual(victim.__str__(), f"{victim.name} - {victim.telephone_number}")

    def test_default_name_is_user(self):
        victim = Victim.objects.create(telephone_number='+256782000000')
        self.assertEqual(victim.name, 'User')