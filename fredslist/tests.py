from django.db.models import Count
from django.test import TestCase, Client
from fredslist.models import State, City, Post
from django.contrib.auth.models import User


# Create your tests here.
class TestStateList(TestCase):
    first_state = State.objects.first()
    second_state = State.objects.last()

    def test_first_state(self):
        self.assertEqual(self.first_state.state, 'Alabama')

    def test_second_state(self):
        self.assertEqual(self.second_state.state, 'Wyoming')


class TestCityDetail(TestCase):
    first_city = City.objects.first()
    last_city = City.objects.last()

    def test_first_city(self):
        self.assertEqual(self.first_city.city, ' auburn')

    def test_second_city(self):
        self.assertEqual(self.last_city.city, '')


class TestPostList(TestCase):
    post1 = Post.objects.first()
    post2 = Post.objects.last()
    post_list = [post1, post2]

    def test_posts_saved_list(self):
        self.assertEqual(len(self.post_list),2)

class TestMyPostList(TestCase):

    def test_user_posts(self):
        c = Client()
        response = c.post('/login/', {'username': 'cesar', 'password': '123'})
        get_posts = c.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(get_posts)

class TestTopPostList(TestCase):
    c = Client()
    all_top_posts = Post.objects.all().annotate(fav_count=Count('favorite')).order_by('-fav_count')

    def test_top_posts(self):
        get_posts = self.c.get('/top_posts/')
        self.assertEqual(get_posts,self.all_top_posts)


# class TestCreatePost(TestCase):
#     def setUp(self):
#         pass

# class TestPostDetail(TestCase):
#     def setUp(self):
#         pass
