from lib.post_repository import PostRepository
from lib.post import Post



"""
test for #all, gets a lists of Post object reflecting seed data
"""

def test_get_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, 'Pixies', 'Rock', 10, 1),
        Post(2, 'ABBA', 'Pop', 2000000, 2),
        Post(3, 'Taylor Swift', 'Pop', 100, 1),
        Post(4, 'Nina Simone', 'Jazz', 0, 3)
    ]


"""
test for #find, gets the Post corresponding the the id
"""

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 'Taylor Swift', 'Pop', 100, 1)