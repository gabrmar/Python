import datetime

from .constants import typography
from .post import Post
from .business import Analytics


class Story(Post, Analytics):
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
            print('*** Story ***')
            print('* Date:', self.created)
            print('* Description:', self.description)
            print('* Emoji:', self.emoji)
            print('* Likes:', self.get_likes())
            print('* Comments:', self.get_comments())
            print('* Tags:', self.tags)
            print('* Typography:', self.typography)
            print('* Background color:', self.background_color)
            print('* Text color:', self.text_color)
        else:
            print('*** Story ***')
            print('* The story has expired')

    def delete(self):
        pass
