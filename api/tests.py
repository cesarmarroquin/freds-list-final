from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from api.views import APIListCreatePost, APIDetailUpdatePost, APIListTopPosts
from fredslist.models import Post, Favorite
from rest_framework.test import APIRequestFactory


class TestAPIListCreatePost(APITestCase):
    def test_list_post__api(self):
        url = reverse('api_post_list_create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass

    def create_post_api(self):
        url = reverse('api_post_list_create')
        data = {postdata}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        pass

class TestAPIDetailUpdatePost(APITestCase):
     def detail_post_api(self):
        url = reverse('api_post_detail_update')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass

class TestAPIListTopPosts(APITestCase):
     def top_post_api(self):
        url = reverse('api_top_post_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pass
