def test_invalid_delete(setup):
    posts_api, _, base_service = setup
    invalid_post_id = 9999
    delete_response = posts_api.delete_post(invalid_post_id)
    base_service.check_status_code(delete_response.status_code, 404)