import random
import datetime

from constants import locations, typography


class Post:
    ''' Superclase Post'''
    def __init__(self, description=None, **kwargs):
        self.description = description
        self.comments = []
        self.likes = 0
        self.author = None

        for llave, valor in kwargs.items():
            setattr(self, llave, valor)


class FeedPost(Post):
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

    def __init__(self, location=None, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)
        self.location = location
        self.active = active
        self.image = []
        self.tags = []


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
        print('Write/Paste your Profile Image.')
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


class Story(Post):
    '''
        This class represents the IG stories that
        dissapear after 24 hours of being published.
    '''
    typography = typography[0]
    emoji = ''
    background_color = '#FFFFFF'
    text_color = '#000000'

    def __init__(self, description=None, active=True, created=None, **kwargs):
        super().__init__(description, **kwargs)
        self.active = active
        self.tags = []
        if not created:
            self.created = datetime.datetime.now()
        else:
            self.created = created

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"

    def get_likes(self):
        return self.likes

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

    def is_valid(self):
        '''
        Show if this story is still in the 24 hours time period.

        You can print a datetime object in a readable format like this:
        self.created.strftime("%B %e, %Y %l:%M %p")
        '''
        diff = datetime.datetime.now() - self.created
        hours_difference = int(diff.total_seconds() // 3600)

        if hours_difference > 24:
            self.active = False
            return False
        return True

    def create(self):
        pass

    def read(self):
        if self.is_valid():
            print('-------- Story --------')
            print('* Date:', self.created)
            print('* Description:', self.description)
            print('* Emoji:', self.emoji)
            print('* Likes:', self.get_likes())
            print('* Comments:', self.get_comments())
            print('* Tags:', self.tags)
            print('* Typography:', self.typography)
            print('* Background color:', self.background_color)
            print('* Text color:', self.text_color)
            print('\n\n')
        else:
            print('-------- Story --------')
            print('* The story has expired')
            print('\n\n')

    def delete(self):
        pass


class Reel(Post):
    video_file = None
    music = None
    visual_effects = None

    def __init__(self, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"

    def get_likes(self):
        return self.likes

    def add_effects(self):
        pass

    def add_music(self):
        pass

    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass


class Live(Post):
    links = None

    def __init__(self, description=None, active=True, **kwargs):
        super().__init__(description, **kwargs)

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"

    def get_likes(self):
        return self.likes

    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass
