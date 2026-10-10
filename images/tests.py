from django.test import TestCase,Client
from django.urls import reverse
from .models import Image
from django.contrib.auth.models import User

class ImagesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser',password='Testing1234')
        self.img = Image.objects.create(user=self.user, title='test image',slug='test',image='G:/NZW/NZW - WEB(BACKEND)/DJANGO 4 BY EXAMPLE/bookmarks/media/users/026/09/26/21455.jpg',url='G:/NZW/NZW - WEB(BACKEND)/DJANGO 4 BY EXAMPLE/bookmarks/media/users/026/09/26/21455.jpg',description='This is a test case.')

    def test_model(self):
        item = Image.objects.get(slug='test')
        self.assertEqual(item.title,'test image')

    def test_item_detail(self):
        url = reverse('images:detail',args=[self.img.id,self.img.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)



class LikeUnlikeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',password='Testing1234')
        self.img = Image.objects.create(user=self.user, title='test image',slug='test',image='G:/NZW/NZW - WEB(BACKEND)/DJANGO 4 BY EXAMPLE/bookmarks/media/users/026/09/26/21455.jpg',url='G:/NZW/NZW - WEB(BACKEND)/DJANGO 4 BY EXAMPLE/bookmarks/media/users/026/09/26/21455.jpg',description='This is a test case.')
        self.client = Client()
        self.client.login(username='testuser',password='Testing1234')

    def test_like_unlike(self):
        url = reverse('images:like')
        response = self.client.post(url,{
            'id':self.img.id,
            'action':'like'
        })
        data = response.json()
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['status'],'ok')
        
        
        