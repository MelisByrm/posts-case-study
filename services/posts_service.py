import requests

from services.base_service import BaseAPI

class PostsAPI(BaseAPI):
    def create_post(self, payload) :
        response = self.post('/posts', payload)
        if response.status_code == 500:
            raise requests.exceptions.HTTPError(f'Server error 500 while creating')
        return response

    def get_all_posts(self):
        response = self.get('/posts')
        if response.status_code == 500:
            raise requests.exceptions.HTTPError(f'Server error 500 while getting posts')
        return response

    def delete_post(self, post_id):
        response = self.delete(f'/posts/{post_id}')
        if response.status_code == 500:
            raise requests.exceptions.HTTPError(f'Server error 500 while deleting a post')
        return response
