import datetime

from instagram import FeedPost, User, Story

user = User(username='pedro_picapiedra')
# homer = User(username='homer_simpson', bio='Family guy from Springfield')

home_feed = []
days_3_ago = datetime.datetime.now() - datetime.timedelta(days=3)


def publish(user):
	post = FeedPost()
	feed_post = post.create(user=user)
	home_feed.append(feed_post)
	return home_feed

'''
publish(user) # 1st post
print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(user) # 2nd post
print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(homer) # 3rd post


user.give_likes(home_feed[0])
homer.give_likes(home_feed[1])
homer.give_likes(home_feed[0])

user.read_posts(home_feed)
'''

# print('\n\n ___________ USERS ___________\n\n')
# user.read()
# homer.read()

# pub = FeedPost('Cali, Colombia','Example Post', active=True, advertisement=False, business=False)


# 3 pruebas con stories

story1 = Story(
	'Campfire at Tayrona Park for the first time',
	emoji=r'''
           (                 ,&&&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \\--._      \\ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,'
      `'(_ )_)(_)_)'
	'''
)
story1.read()

story2 = Story('Probably an expired story', emoji=':(', created=days_3_ago)
story2.read()

story3 = Story(
	'Walking Toby',
	emoji=r'''
            __
(\,--------'()'--o
 (_    ___    /~"
  (_)_)  (_)_)
	'''
)
story3.read()

