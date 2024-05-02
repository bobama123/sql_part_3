from lib.post import Post

"""
Test for id, title, content, no_of_views and user_account_id
"""

def test_post_constructs():
    post = Post(4, 'Nina Simone', 'Jazz', 0, 3)
    assert post.id == 4
    assert post.title == 'Nina Simone'
    assert post.content == 'Jazz'
    assert post.no_of_views == 0
    assert post.user_account_id == 3


"""
Test to compare 2 equal posts
"""

def test_posts_are_equal():
    post1 = Post(4, 'Nina Simone', 'Jazz', 0, 3)
    post2 = Post(4, 'Nina Simone', 'Jazz', 0, 3)
    assert post1 == post2


"""
test to format posts nicely
"""

def test_for_post_format():
    post = Post(4, 'Nina Simone', 'Jazz', 0, 3)
    assert str(post) == "Post(4, Nina Simone, Jazz, 0, 3)"