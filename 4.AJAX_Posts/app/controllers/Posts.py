
from system.core.controller import *

class Posts(Controller):
    def __init__(self, action):
        super(Posts, self).__init__(action)
        self.load_model('Post')
        self.db = self._app.db
    def index(self):
        return self.load_view('index.html')
    def index_json(self):
        posts = self.models['Post'].index()
        return jsonify(posts=posts)
    def index_html(self):
        posts = self.models['Post'].index()
        return self.load_view('partials/post.html', posts=posts)
    def create(self):
        self.models['Post'].create(request.form)
        posts = self.models['Post'].index()
        return self.load_view('partials/post.html', posts=posts)
