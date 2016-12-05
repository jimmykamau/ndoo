from django.test import TestCase, Client


class TestRouting(TestCase):

    def setUp(self):
        self.client_stub = Client()

    def test_view_bucketlists_route(self):
        response = self.client_stub.get(
            '/api/v1/bucketlists/')
        self.assertEquals(response.status_code, 403)

    def test_create_bucketlist_route(self):
        response = self.client_stub.post(
            '/api/v1/bucketlists/')
        self.assertEquals(
            response.status_code, 403)

    def test_update_bucketlist_route(self):
        response = self.client_stub.put(
            '/api/v1/bucketlists/')
        self.assertEquals(
            response.status_code, 403)

    def test_delete_bucketlist_route(self):
        response = self.client_stub.delete(
            '/api/v1/bucketlists/')
        self.assertEquals(
            response.status_code, 403)

    def test_view_bucketlistitems_route(self):
        response = self.client_stub.get(
            '/api/v1/bucketlists/1/items/')
        self.assertEquals(response.status_code, 403)

    def test_create_bucketlistitems_route(self):
        response = self.client_stub.post(
            '/api/v1/bucketlists/1/items/')
        self.assertEquals(
            response.status_code, 403)

    def test_update_bucketlistitems_route(self):
        response = self.client_stub.put(
            '/api/v1/bucketlists/1/items/')
        self.assertEquals(
            response.status_code, 403)

    def test_delete_bucketlistitems_route(self):
        response = self.client_stub.delete(
            '/api/v1/bucketlists/1/items/')
        self.assertEquals(
            response.status_code, 403)
