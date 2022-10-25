from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .models import Post


# Create your tests here.
class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='post1',
            description = 'this is test',
            text='this is text',
            author=cls.user,
            status=Post.STATUS_CHOICE[0][0],
        )

        cls.post2 = Post.objects.create(
            title='post2',
            description='loream spum 2',
            text='this is text for post 2',
            author=cls.user,
            status=Post.STATUS_CHOICE[1][0],
        )

    def test_post_str(self):
        post = self.post1
        self.assertEqual(str(post), 'post1')

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'post1')
        self.assertEqual(self.post1.description, 'this is test')

    def test_post_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_status_404_for_page_not_exit(self):
        response = self.client.get(reverse('post_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_page_details_by_name_url(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_page_details_has_content(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)

    def test_page_details_with_url_has_content(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)

    def test_post_draft_not_show_on_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('add_post'), {
            'title': 'some title',
            'description': 'some description',
            'text': 'some text',
            'author': self.user.id,
            'status': 'pub'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')

    def test_post_update_view(self):
        response = self.client.post(reverse('update_post', args=[self.post2.id]), {
            'title': 'updated title',
            'description': 'updated description',
            'text': 'updated text',
            'author': self.user.id,
            'status': 'pub'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'updated title')

    def test_post_delete_view(self):
        response = self.client.post(reverse('delete_post', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)
