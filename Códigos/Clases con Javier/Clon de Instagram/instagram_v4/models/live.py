from .post import Post
from .business import Analytics


class Live(Post, Analytics):
    links = None

    def __init__(self, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)

    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass
