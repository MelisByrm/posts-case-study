import uuid

import pytest

from services.base_service import BaseAPI
from services.posts_service import PostsAPI
from services.comments_service import CommentsAPI
from utils.config import load_test_data
import random

@pytest.fixture
def setup():
    posts_api = PostsAPI()
    comments_api = CommentsAPI()
    base_service =  BaseAPI()
    return posts_api, comments_api, base_service

def e2e_test_create_get_comment_delete(setup):
    posts_api, comments_api, base_service = setup
    test_data = load_test_data('posts_data.json')

    valid_post = test_data['default_post'].copy()
    valid_post['id'] = str(uuid.uuid4())
    valid_post['userId'] = 1

    response = posts_api.create_post(valid_post)
    base_service.check_status_code(response.status_code, 201)
    input_content = valid_post.items()
    new_post_response = response.json()
    base_service.compare_response_and_input(input_content, new_post_response)
    if 'id' not in new_post_response:
        raise ValueError('Response is missing the id field')
    post_id = new_post_response['id']

    response = comments_api.get_comments_for_post(post_id)
    base_service.check_status_code(response.status_code, 200)
    assert len(response.json()) == 0

    all_posts = posts_api.get_all_posts().json()
    random_post = random.choice(
        [post for post in all_posts if post['id'] != post_id]
    )
    random_post_comments = comments_api.get_comments_for_post(random_post['id'])
    base_service.check_status_code(random_post_comments.status_code, 200)

    delete_response = posts_api.delete_post(post_id)
    base_service.check_status_code(delete_response.status_code.status_code, 200)

    updated_posts = posts_api.get_all_posts().json()
    assert not any(post['id'] == post_id for post in updated_posts)

    deleted_post_comments = comments_api.get_comments_for_post(post_id)
    base_service.check_status_code(deleted_post_comments.status_code, 404)