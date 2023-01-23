import random

from .constants import locations
from .post import Post
from .story import Story
from .business import Analytics
from .exceptions import NoImageFoundError


class FeedPost(Post, Analytics):
    """
    --- This is a docstring to document code. ---
    This class is about the posts that goes inside
    the newsfeed of Instagram.
    """    
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

    def __init__(self, location=None, description=None, active=True, image=[], tags=[], **kwargs):
        super().__init__(description, **kwargs)
        self.location = location
        self.active = active
        self.image = image
        self.tags = tags

        if not self.image:
            raise NoImageFoundError(
                "An image is required to create a FeedPost"
            )

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
            for line in self.image:
                if line:
                    print(line)
            print('')

    def tag_people(self):
        if not self.tags:
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

        if isinstance(self.image, list):
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
        print('*** FeedPost ***')
        print('* Location:', self.location)
        print('* Image:')
        print('')
        if isinstance(self.image, list):
            self.show_image()
        else:
            print(self.image)
        print('* Description:', self.description)
        print('* Likes:', self.get_likes())
        print('* Comments:', self.get_comments())
        print('* Tags:', self.tags)

    def update(self):
        pass

    def delete(self):
        pass


class SuperPost(FeedPost, Story):
    def __init__(self, admin_name=None, **kwargs):
        super().__init__(**kwargs)
        self.admin_name = admin_name

