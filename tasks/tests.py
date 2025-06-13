from rest_framework.test import APITestCase
from .models import Task


class TaskViewSetFilterTest(APITestCase):
    def setUp(self):
        Task.objects.create(
            title="Buy milk",
            description="2 bottles",
            priority="MEDIUM",
            is_completed=False,
        )
        Task.objects.create(
            title="Buy bread",
            description="Whole gain",
            priority="MEDIUM",
            is_completed=True,
        )

    def test_filter_by_search(self):
        response = self.client.get("/api/tasks/?search=milk")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Buy milk")

    def test_ordering_by_completion(self):
        response = self.client.get("/api/tasks/?ordering=is_completed")
        self.assertEqual(response.status_code, 200)
        titles = [task["title"] for task in response.data]
        self.assertEqual(titles, ["Buy milk", "Buy bread"])
