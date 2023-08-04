from imdb import IMDb

# Create an instance of the IMDb class
ia = IMDb()

def print_imdb_actor_page(actor_name):
    # Search for actors with the given name
    search_results = ia.search_person(actor_name)
    
    if search_results:
        # Get the first search result (assumes the most relevant match)
        actor = search_results[0]
        actor_id = actor.personID
        actor_url = f"https://www.imdb.com/name/nm{actor_id}/"
        return(actor_url)
    else:
        return(f"No IMDb record found for {actor_name}")


