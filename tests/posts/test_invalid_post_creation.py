from utils.config import load_test_data

def test_post_creation_without_id(setup):
    posts_api, _, base_service = setup
    test_data = load_test_data('posts_data.json')

    invalid_post_data = test_data['missing_id']
    response = posts_api.create_post(invalid_post_data)
    base_service.check_status_code(response.status_code, 200)
