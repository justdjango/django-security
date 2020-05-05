from django.contrib.auth import get_user_model
from accounts.models import Column

User = get_user_model()


class ColumnTestDataMixin(object):
    @classmethod
    def setUpTestData(cls):
        coordinator = User.objects.create_user(username="coordinator",
                                               email="coordinator@test.com", password="test1234")
        moderator = User.objects.create_user(username="moderator",
                                             email="moderator@test.com", password="test1234")
        writer = User.objects.create_user(username="writer",
                                          email="writer@test.com", password="test1234")

        column = Column.objects.create(
            name="Test column",
            coordinator=coordinator
        )
        column.moderators.add(moderator)
        column.writers.add(writer)
