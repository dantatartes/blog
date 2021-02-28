from django.test import TestCase
from django.contrib.auth.models import User
import datetime
import pytz
from .models import Post

TIME = pytz.timezone("Europe/Moscow").localize(datetime.datetime(2021, 2, 28, 11, 4, 36, 297119))


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        admin = User.objects.create_superuser('ADMIN', 'ADMIN@ADMIN.com', "ADMIN")
        Post.objects.create(title='Test',
                            preview='test preview',
                            slug='test_slug',
                            author=admin,
                            publish=TIME,
                            content='test content',
                            status='publish'
                            )

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_preview_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('preview').verbose_name
        self.assertEqual(field_label, 'preview')

    def test_slug_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_author_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_publish_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('publish').verbose_name
        self.assertEqual(field_label, 'publish')

    def test_content_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_status_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 250)

    def test_status_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('status').max_length
        self.assertEqual(max_length, 10)

    def test_object_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test')

    def test_object_preview(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.preview, 'test preview')

    def test_object_slug(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.slug, 'test_slug')

    def test_object_author(self):
        post = Post.objects.get(id=1)
        user, created = User.objects.get_or_create(username='ADMIN')
        self.assertEqual(False, created)
        self.assertEqual(post.author, user)

    def test_object_publish(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.publish, TIME)

    def test_object_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'test content')

    def test_object_status(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.status, 'publish')

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.get_absolute_url(), '/test_slug/')

