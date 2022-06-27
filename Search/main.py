import animec

query = input("Enter anime name : ")

try:
    anime = animec.Anime(query)
except:
    print(f"404 : No Anime Found - {query}")

print(f"Title : {anime.title_english}")
print(f"URL : {anime.url}\n\n\n")
print(f"{anime.description}\n\n\n")
print(f"Total Episodes : {str(anime.episodes)}")
print(f"Rating : {str(anime.rating)}")
print(f"Broadcast : {str(anime.broadcast)}")
print(f"Status : {str(anime.status)}")
print(f"Type : {str(anime.type)}")
print(f"NSFW Status : {str(anime.is_nsfw())}")