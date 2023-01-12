from Instapy import FeedPost

feed = FeedPost()


feed.description = "hola nuevo"

feed2 = FeedPost

print(feed.description)
print(feed2.description)

del feed2 #Borra objeto feed2

x = feed.get_location()
print(x)
print(FeedPost.get_location(feed)) #Debe dar la misma dirección de memoria ya que estmaos usando la misma instancia de la clase FeedPost

print(feed.show_comments())
feed.comments.append("galleta voladora")
feed.comments.append("Me gusta mucho este contenido de calidad")
print(feed.show_comments())