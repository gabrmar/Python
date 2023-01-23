import datetime

from models.feedpost import FeedPost, SuperPost
from models.user import User, Address
from models.story import Story
from models.reel import Reel
from models.live import Live
from models.photos import (
    BATMAN,
    HOMER_SIMPSON,
    BENDER,
    METROPOLIS,
    GOLDEN_GATE,
    BEACH,
    MARACAIBO,
    LOS_ANDES,
    PUERTO,
    CALI,
    EARTH,
    CAMP_FIRE,
    TOBY,
    BARRANQUILLA
)
from models.exceptions import NoImageFoundError, InvalidAudioFile

user = User(
    username='batman',
    bio='The Dark Knight',
    image=BATMAN,
    followers=500000,
)
homer = User(
    username='homer_simpson',
    bio='Family guy from Springfield',
    image=HOMER_SIMPSON,
    address='Springfield'
)

user.address = Address(
    '121 avenida los nogales', 
    'Bello', 
    'Antioquia', 
    '03301'
)

user2 = User(
    'bender',
    bio='Character from the TV series Futurama',
    image=BENDER
)

direccion = Address(
    'Edificio Mirador del Mar, avenida Los cocos', 
    'Cartagena', 
    'Bolívar', 
    '201918'
)

user2.address = direccion



home_feed = []
days_3_ago = datetime.datetime.now() - datetime.timedelta(days=3)


def publish(user, photo=None, *args, **kwargs):
	post = FeedPost(image=photo, **kwargs)
	feed_post = post.create(user=user)
	home_feed.append(feed_post)
	return home_feed

# 1st post
publish(
    user,
    photo=METROPOLIS,
    description="A picture from Superman's city",
    location='Metropolis, Illinois',
    tags=['Superman', 'Wonderwoman'],
)
# print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(
    user,
    photo=GOLDEN_GATE,
    description="A picture of San Francisco's golden gate at the morning",
    location='San Francisco, California',
    tags=['Batman', 'Robin', 'Batwoman']
)
# print('\n\n -------- Create a new post for Instagram ---------\n\n')
publish(
    homer,
    photo=BEACH,
    description="Vacations for the Simpsons family in Cancún",
    location='Cancún, México',
    tags=['Homer', 'Marge', 'Lisa', 'Maggie', 'Bart']
)


user.give_likes(home_feed[0])
homer.give_likes(home_feed[1])
homer.give_likes(home_feed[0])


pub = FeedPost(
    'Cali, Colombia',
    'Example Post',
    active=True,
    advertisement=False,
    business=False,
    image=CALI
)
home_feed.append(pub)

# 3 pruebas con stories

story1 = Story(
	'Campfire at Tayrona Park for the first time',
	emoji=CAMP_FIRE
)
home_feed.append(story1)

story2 = Story('Probably an expired story', emoji=':(', created=days_3_ago)
home_feed.append(story2)

story3 = Story(
	'Walking Toby',
	emoji=TOBY
)
home_feed.append(story3)


# print('\n\n ___________ BUSINESS TEST BEGINS ___________\n\n')


pub = FeedPost(
    'International Space Station, Outer space',
    'Picture of planet Earth from the ISS',
    active=True,
    advertisement=False,
    business=False,
    image=EARTH
)

pub2 = FeedPost(
    'Barranquilla, Colombia',
    'Example post 2',
    active=True,
    number_of_views=16,
    image=BARRANQUILLA
)
pub3 = FeedPost(
    'Puerto Colombia, Colombia',
    'Example post of Puerto Colombia',
    active=True,
    number_of_views=70,
    image=PUERTO
)

pub4 = FeedPost(
    'Maracaibo, Venezuela',
    'La fotaza desde Maracaibo',
    image=MARACAIBO,
    active=True,
    number_of_views=99
)

home_feed.append(pub4)
home_feed.append(pub2)
home_feed.append(pub)
home_feed = user.promotion_post(pub, home_feed)
home_feed = user.promotion_post(pub3, home_feed)

# print('\n\n ___________ SUPERPOST TEST BEGINS ___________\n\n')



sp = SuperPost(
    location='Meta, Cundinamarca',
    description='Descripción arbitraria',
    admin_name='Filippo Gana',
    image=LOS_ANDES
)

home_feed.append(sp)
user.read_posts(home_feed)



# print('\n\n', '___________ USERS ___________','\n\n')
# user.read()
# homer.read()
# user2.read()

print('\n\n ___________ Subclass of ANALYTICS TEST ___________\n\n')

story1.number_of_views = 30
print('* Overview of Story #1', story1.overview())

reel = Reel(
    "guns_roses.mp3",  # Relacion de composición
    description='First Reel everrrr!',
    number_of_views=55
)
print('* Overview of Reel', reel.overview())
print('Archivo del Reel', reel.music)

live = Live(
    description='Javier Meetup: Create your Python portfolio for getting job offers',
    number_of_views=30,
)

print('* Overview of Live', live.overview())


print('\n\n ___________ Audio files TEST ___________\n\n')

reel = Reel(
    "AC_DC_thunderstruck.mp3",
    description='first Reeel ever!!',
    number_of_views=55
)

print(reel.music)


print('\n\n ___________ TEST AudioFileException ___________\n\n')

try:
    reel2 = Reel(
        "AC_DC_thunderstruck.wav",
        description='first Reeel ever!!',
        number_of_views=55
    )
except InvalidAudioFile as e:
    print(e)


print('\n\n ___________ TEST No Image Exception ___________\n\n')

try:
    pub5 = FeedPost(
        'International Space Station, Outer space',
        'Picture of planet Earth from the ISS',
        active=True,
        advertisement=False,
        business=False,
    )
except NoImageFoundError as error:
    # TODO: Write error inside logs file
    print(error)


# if __name__ == '__main__':
#     # home_feed = []
#     # days_3_ago = datetime.datetime.now() - datetime.timedelta(days=3)

#     user, homer, user2 = user_creation()
#     main(publish, days_3_ago, home_feed, user=user, homer=homer, user2=user2)

