import requests

from services.base_service import BaseAPI

class CommentsAPI(BaseAPI):
    def get_comments_for_post(self, post_id):
        response = self.get(f'/comments', params={'postId': post_id})
        if response.status_code == 500:
            raise requests.exceptions.HTTPError(f'Server error 500 from comments endpoint')
        return response
