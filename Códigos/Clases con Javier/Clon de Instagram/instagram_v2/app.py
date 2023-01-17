from instagram import FeedPost, User

# post = FeedPost()
# post.show_filters()
# print('\n\n')
# post.create()
# post.read()

user = User(username='pedro_picapiedra')
homer = User(username='homer_simpson', bio='Family guy from Springfield')

home_feed = []

def publish(user):
	post = FeedPost()
	feed_post = post.create(user=user)
	home_feed.append(feed_post)
	return home_feed

publish(user) # 1st post
print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(user) # 2nd post
print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(homer) # 3rd post


user.give_likes(home_feed[0])
homer.give_likes(home_feed[1])
homer.give_likes(home_feed[0])

user.read_posts(home_feed)


print('\n\n ___________ USERS ___________\n\n')
user.read()
homer.read()
