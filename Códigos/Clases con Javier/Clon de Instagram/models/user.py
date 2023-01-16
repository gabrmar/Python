from .business import Business


class User(Business):
    ''' Instagram User '''
    followers = 0
    following = 0
    address = None

    def __init__(self, username=None, bio=None, image=[], **kwargs):
        self.username = username
        if bio:
            self.bio = bio
        else:
            self.bio = None
        self.image = image
        self.posts = []

        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.load_image():
            print('* Profile image uploaded successfully \n\n')
        else:
            print('No profile image was uploaded \n\n')

    def load_image(self):
        if self.image:
            return True

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
            for line in self.image:
                if line:
                    print(line)
            print('')

    def give_likes(self, post):
        post.likes += 1
        return True

    def read_posts(self, feed):
        print('='*70)
        print('='*20,'HOME FEED', '='*20)
        print('='*70, end='\n\n')
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
        print('* Image:')
        print('')
        if isinstance(self.image, list):
            self.show_image()
        else:
            print(self.image)
        print('* Biography:', self.bio)
        print('* Followers:', self.followers)
        print('* Following:', self.following)
        print('* Address:', self.address)
        print('\n\n')

    def update(self):
        pass

    def delete(self):
        pass


class Address:
    """
    This class was taken from the book
    """
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)


class MultiLingualAdress:
    # aceptar direcciones en varios idiomas
    pass

