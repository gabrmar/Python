import random


class Business:
    '''
    A User can upgrade it's category and promote posts
    '''
    business_account = True

    def __init__(self, business_account=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_account = business_account

    def promotion_post(self, pub, feed):
        '''Add the post to the beggining of the feed'''
        try:
            index = feed.index(pub)
        except ValueError:
            print('The post is not in the list \n')
        else:
            del feed[index]

        feed.insert(0, pub)
        return feed


class Analytics:
    number_of_views = 0
    accounts_reached = 0

    def __init__(self, number_of_views=0, accounts_reached=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number_of_views = number_of_views
        self.accounts_reached = accounts_reached

    def overview(self):
        if self.number_of_views != 0:
            return f'You reached + {random.randint(self.number_of_views, 100)}% more accounts'
