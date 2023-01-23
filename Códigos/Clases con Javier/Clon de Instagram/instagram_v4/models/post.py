class Post:
    ''' Superclase Post'''
    def __init__(self, description=None, **kwargs):
        self.description = description
        self.comments = []
        self.likes = 0
        self.author = None

        for llave, valor in kwargs.items():
            setattr(self, llave, valor)

    def get_likes(self):
        return self.likes

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"
