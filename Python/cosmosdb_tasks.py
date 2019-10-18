import json


def task1():
    # Create a database database named moviesDatabase with containers moviesContainer , audioContainer, imageContainer
    # Write code that lists out the names of all the containers in the moviesDatabase
    pass



def task2():
    # Write code that inserts a new records into the movie database
    # {
    #   "title": "Mary Queen of Scots",
    #   "year": 2017,
    #   "cast":
    #       ["Saoirse Ronan",
    #       "Margot Robbie"],
    #   "genres":
    #       ["Historical",
    #       "Drama"]
    # }
    #{
    #   "title": "The Enchanted Drawing",
    #   "year": 1900,
    #   "cast":
    #       [Albert E. Smith],
    #   "genres":
    #       ["Fiction",
    #       "Drama"]
    # }
    pass


def task3():
    # Write code that queries the database for the "Mary Queen of Scots" movie that you just inserted
    # Use the following query to find the movie by the title: "SELECT * FROM c WHERE c.title = 'Mary Queen of Scots'"
    # If you find the movie, print out the details of the movie to the console
    pass


def task4():
    # Write code that queries the movies database for all movies that contain the word Scotland in the title
    # Print out the details of any movies that you find
    # Use the following query: SELECT * FROM c WHERE CONTAINS(c.title, 'Scotland')
    pass


def task5():
    # Write code that updates the entry for movie 'The Enchanted Drawing' so that the cast list includes 'J. Stuart Blackton'
    pass

def task6():
    # Write code that iterates through all of the movies in the database and counts how many movies there are per year
    # Find a way to output the number of request units that were consumed to perform this operation
    movieStats = {}


    #for every movie in the database
        # if movieStats.get(movie['year'], 0) == 0:
        #     movieStats[movie['year']] = 1
        # else:
        #     movieStats[movie['year']] = movieStats[movie['year']] + 1
    
    for stats in movieStats:
        print(str(stats) + ' ' +  str(movieStats[stats]))

    # Write code to determine what the actual charge was
    charge = 0
    print("The operation used " + charge + " request units")

def task7():
    # Write code that retrieves and prints the throughput of the movies container
    # If the throughput of the container is not already 500 RUs, then set it to 500 RUs
    pass

def task8():
    # Write code that deletes the items you added in task 2
    pass

def task9():
    # Write code that deletes the Scontainer you created in task 1
    pass

def task13():
    # Write code that deletes the database you created in task 1
    pass

task1()