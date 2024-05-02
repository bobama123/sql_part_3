from lib.post import Post

class PostRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(
                row["id"],
                row["title"],
                row["content"],
                row["no_of_views"],
                row["user_account_id"])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(
            row["id"],
            row["title"],
            row["content"],
            row["no_of_views"],
            row["user_account_id"])