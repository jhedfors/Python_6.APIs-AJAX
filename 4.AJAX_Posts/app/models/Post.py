from system.core.model import Model

class Post(Model):
    def __init__(self):
        super(Post, self).__init__()
    def index(self):
        query = "SELECT * FROM posts"
        values = {}
        return self.db.query_db(query,values)
    def create(self,post):
        query = "INSERT INTO posts (post,created_at,updated_at) VALUES (:post,NOW(),NOW())";
        values = {'post': post['post'] }
        return self.db.query_db(query,values)
