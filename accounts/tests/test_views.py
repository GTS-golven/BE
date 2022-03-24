from django.urls import reverse

from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_cannot_register_without_data(self):
        response = self.client.post(self.user_create)
        
        self.assertEqual(response.status_code, 400)
        
    def test_can_register_with_username_password(self):
        response = self.client.post(
            self.user_create, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_can_register_with_username_password_name(self):
        data = {**self.user_data, **self.user_first_and_last_name }
        response = self.client.post(
            self.user_create, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_can_change_username(self):
        response = self.client.patch(
            reverse('user-get', args=[self.user.id]), 
            self.user_updated_username
        )
        self.assertEqual(response.status_code, 200)
        
    def test_can_change_password(self):
        response = self.client.patch(
            reverse('user-get', args=[self.user.id]), 
            self.user_updated_password
        )
        self.assertEqual(response.status_code, 200)
        
    def test_can_set_first_and_last_name(self):
        response = self.client.patch(
            reverse('user-get', args=[self.user.id]),
            self.user_first_and_last_name
        )
        self.assertEqual(response.status_code, 200)
        
    def test_can_delete(self):
        response = self.client.delete(
            reverse('user-get', args=[self.user.id])
        )
        self.assertEqual(response.status_code, 204)
        
    def test_can_upload_picture(self):
        payload = {
            'videofile': self.file
        }
        
        response = self.client.patch(
            reverse('user-get', args=[self.user.id]),
            payload
        )
        
        self.assertEqual(response.status_code, 200)