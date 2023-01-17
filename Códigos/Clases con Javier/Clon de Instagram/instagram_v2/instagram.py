import random


locations = [
    'Barranquilla, Colombia',
    'Bogotá, Colombia',
    'Miami, USA',
    'Disney World, Orlando',
    'Cabo Cañaveral, Orlando',
    'Ciudad de Panamá, Panamá',
    'Tokyo, Japón',
]


class FeedPost:
    """
    --- This is a docstring to document code. ---
    This class is about the posts that goes inside
    the newsfeed of Instagram.
    """
    description = None
    location = None
    likes = 0
    filters = [
        'MayFair',
        'Amaro',
        'Clarendan',
        'Gingham',
        'Moon',
        'Lark',
        'Reyes',
        'Perpetua',
    ]

    def __init__(self, location=None, description=None, tag=None, **kwargs):
        if location:
            self.location = location
        if description:
            self.description = description
        if tag:
            self.tags.append(tag)
        self.image = []
        self.comments = []
        self.tags = []
        self.author = None

        for llave, valor in kwargs.items():
            setattr(self, llave, valor)

    def get_location(self, position=None):
        '''
        Position is an int
        '''

        if position:
            try:
                return locations[position]
            except IndexError:
                print('The position is out of the range')
                return None
            except TypeError:
                print('Please write just integer numbers')
                return None

        return random.sample(locations, 1)[0]

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"

    def get_likes(self):
        return self.likes

    def show_filters(self):
        print('* Available filters are:')
        for filter in self.filters:
            print('  -', filter)

    def load_image(self):
        print('Write/Paste your image.')
        print('Use Ctrl-D or Ctrl-Z ( windows ) to save it.')

        while True:
            try:
                line = input()
            except EOFError:
                break
            else:
                self.image.append(line)

        try:
            if line:
                return True
        except UnboundLocalError:
            print('Blank image')
            return False

    def apply_filter(self):
        pass

    def show_image(self):
        if self.image:
            print('* Image:')
            print('')
            for line in self.image:
                if line:
                    print(line)
            print('')

    def tag_people(self):
        print('')
        print("Write your friends's names one by one.")
        print("Use Ctrl-D or Ctrl-Z ( windows ) to save it.")
        print('')
        while True:
            try:
                line = input('> ')
            except EOFError:
                break
            self.tags.append(line)


    def create(self, user):

        if self.load_image():
            print('* Image saved successfully')
        else:
            print('No image was uploaded')
            return False

        if not self.location:
            opcion = int(input('Choose:\n1. Write a location\n 2. Get a location randomly\n> '))
            
            if opcion == 1:
                chosen_location = input('Please write a location for your post')
            else:
                chosen_location = self.get_location()
            self.location = chosen_location

        if not self.description:
            self.description = input('Please write a description: ')

        self.tag_people()
        self.author = user
        user.posts.append(self)

        return self

    def read(self):
        print('\n\n')
        print('* Location:', self.location)
        self.show_image()
        print('* Description:', self.description)
        print('* Likes:', self.get_likes())
        print('* Comments:', self.get_comments())
        print('* Tags:', self.tags)
        print('\n\n')

    def update(self):
        pass

    def delete(self):
        pass


class User:
    ''' Instagram User '''
    followers = 0
    following = 0

    def __init__(self, username, bio=None, **kwargs):
        self.username = username
        if bio:
            self.bio = bio
        else:
            self.bio = None
        self.image = []
        self.posts = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.load_image():
            print('* Profile image uploaded successfully \n\n')
        else:
            print('No profile image was uploaded \n\n')

    def load_image(self):
        print('Write/Paste your image.')
        print('Use Ctrl-D or Ctrl-Z ( windows ) to save it.')

        while True:
            try:
                line = input()
            except EOFError:
                break
            else:
                self.image.append(line)

        try:
            if line:
                return True
        except UnboundLocalError:
            print('Blank image')
            return False

    def show_image(self):
        if self.image:
            print('* Image:')
            print('')
            for line in self.image:
                if line:
                    print(line)
            print('')

    def give_likes(self, post):
        post.likes += 1
        return True

    def read_posts(self, feed):
        for publication in feed:
            publication.read()
            print('\n\n --------------- \n\n')

    def give_comments(self):
        pass

    def create(self):
        pass

    def read(self):
        print('\n\n')
        print('* Username:', self.username)
        self.show_image()
        print('* Biography:', self.bio)
        print('* Followers:', self.followers)
        print('* Following:', self.following)
        print('\n\n')

    def update(self):
        pass

    def delete(self):
        pass
