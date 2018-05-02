import random

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    movielist = ["Star Wars", "Hobbit", "Harry Potter and the Sorceror's Stone",
                 "Harry Potter and the Prisoner of Azkhaban", "The Empire Strikes Back", "The Fellowship of the Ring",
                 "The Two Towers", "The Return of the King"]

    goodmovie = random.choice(movielist)
    return goodmovie

print(get_random_movie())