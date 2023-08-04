from imdb import IMDb
from imdb_ref import print_imdb_actor_page

# Create an IMDb instance
ia = IMDb()

# Search for a movie by title
movie_title = "Eyes Wide Shut"
movies = ia.search_movie(movie_title)

# # Print information about the first search result
# if movies:
#     first_movie = movies[0]
#     ia.update(first_movie)
#     print("Title:", first_movie["title"])
#     print("Year:", first_movie["year"])
#     print("Genres:", first_movie["genres"])
#     print("Rating:", first_movie["rating"])
# else:
#     print("No results found for", movie_title)


if movies:
    # Get the first search result (movie)
    first_movie = movies[0]
    
    # Update the movie details
    ia.update(first_movie, info=['main', 'cast'])
    
    print("Title:", first_movie["title"])

    
    # Print the list of actors and their roles
    for actor in first_movie["cast"]:
        url = print_imdb_actor_page(actor["name"])
        print("<role>",actor.currentRole,"</role>")
        print("<actor ref='",f"{url}" ,"'>", actor["name"],"<actor>")
        print("---")
else:
    print("No results found for", movie_title)


