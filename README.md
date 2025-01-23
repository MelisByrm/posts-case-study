# CASE STUDY FOR POSTS API
## Setup Requirements

### Tools and Languages Used
- **Python**  
- **requests**  
- **pytest**  

### Python Version
- Python 3.11 and above  

### Installation
Use `pip` to set up the required dependencies:  
```bash
pip install -r requirements.txt
```

## **NOTE !!** 
_Since the API shared acts as fake API none of the actions (eg. create delete) is applied and visible. So returned error codes are assumption. Also when this automation runs it'll be fail since assertions will fail since no action is reflected to the API._

### Scenarios :

#### E2E  :

(This scenario covers creation, deletion, getting comments and getting the posts.)
User creates a post, reads other user's posts, delete's the post they created and then make sure it's deleted.
    Steps :
    1. Create a post.
    2. Get comments of another user.
    3. Get all the posts and picking a random post delete the post.
    4. Make sure it's deleted.
    5. Try to get deleted post's comments.

#### Negative cases :

1. Delete a post with not existed id, understandable error should return and action should fail.
2. Create a post with missing content and make bad request has been returned and post hadn't created.

    