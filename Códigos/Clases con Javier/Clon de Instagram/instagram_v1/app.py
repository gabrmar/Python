from instagram import FeedPost


el_feed = FeedPost()

print('You have currently', el_feed.get_likes(), 'likes')
el_feed.show_filters()
print('\n\n\n')

el_feed.post()
el_feed.read()

