class Post:
    
    def __init__(self, id, title, content, no_of_views, user_account_id):
        self.id = id
        self.title = title
        self.content = content
        self.no_of_views = no_of_views
        self.user_account_id = user_account_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.no_of_views}, {self.user_account_id})"