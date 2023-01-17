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
    """This is a docstring to document code.
    This class is about the posts that goes inside
    the newsfeed of Instagram"""
    image = []
    description = None
    location = None
    likes = 0
    comments = []
    tags = []
    filters = [
        'MayFair',
        'Amaro',
        'Clarendan',
        'Gingham',
        'Moon',
        'Lark',
        'Reyes',
        'Perpetua'
    ]

    def get_location(self):
        # print("Called by {}".format(self))
        return random.sample(locations, 1)[0]

    def get_comments(self):
        if self.comments:
            return self.comments
        else:
            return "This post has no comments"

    def get_likes(self):
        return self.likes

    def show_filters(self):
        print('Available filters are:')
        for the_filter in self.filters:
            print('*', the_filter)

    def load_image(self):
        print("Write/Paste your image.") 
        print("Use Ctrl-D or Ctrl-Z ( windows ) to save it.")
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
            print('blank image')
            return False

    def show_image(self):
        if self.image:
            # print('The image is:')
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

    def post(self):
        """
        Post method for the FeedPost class
        
        input: nothing
        output: Returns True if everything was created successfully
                or False in case of an exception happened.
        """

        if self.load_image():
            print("Image saved successfully")
        else:
            print('No image was uploaded.')
            return False

        self.location = self.get_location()
        self.description = input('Please write a description: ')
        self.tag_people()
        
        '''
        if not self.location:
            self.location = self.get_location()
        if not self.description:
            print('Your current description is ', self.description)
            self.description = input('Please write a description: ')
        '''

        return True

    def read(self):
        print('\n\n')
        print(self.location)
        self.show_image()
        print(self.description)
        print(self.likes, 'likes')
        self.get_comments()
        print('tags:', self.tags)
        print('\n\n')

    def edit(self):
        pass

    def image_filter(self):
        pass

    def delete(self):
        pass
