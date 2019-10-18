import json
import azure.cosmos.errors as errors
from azure.cosmos.cosmos_client import CosmosClient
from azure.cosmos.partition_key import PartitionKey
from azure.cosmos.diagnostics import RecordDiagnostics



def task1():
    # Write code that creates a database named UXStudyDatabase and a container in that database named UXResearchers
    # Set the database up so that it has a throughput of 500 request units (RUs).
    # Then add the following two items to the UXResearchers container  
    # {"name": "Steven", "Office": "Edinburgh"}
    # {"name": "Drew", "Office": "Redmond"}
    pass

def task2():
    # There is a database named moviesDatabase
    # Write code that lists out the names of all the containers in the moviesDatabase
    pass


def task3():
    # The movies database contains a container named moviesContainer that contains information about thousands of movies
    # Each movie looks similar to the following
    # {
    #     "title": "The Automobile Thieves",
    #     "year": 1906,
    #     "cast": [
    #         "J. Stuart Blackton",
    #         "Florence Lawrence"
    #     ],
    #     "genres": [
    #         "Short",
    #         "Crime",
    #         "Drama"
    #     ],
    #     "id": "242",
    #     "_rid": "f01KALuEsCbzAAAAAAAAAA==",
    #     "_self": "dbs/f01KAA==/colls/f01KALuEsCY=/docs/f01KALuEsCbzAAAAAAAAAA==/",
    #     "_etag": "\"74007f98-0000-0c00-0000-5d00e2cb0000\"",
    #     "_attachments": "attachments/",
    #     "_ts": 1560339147
    # }
    # Write code that connects to this database and prints out the number of movies that are stored in the movies container
    pass


def task4():
    # Write code that inserts a new record into the movie database
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
    pass

def task5():
    # Write code that queries the database for the movie that you just inserted
    # Use the following query to find the movie by the title: "SELECT * FROM c WHERE c.title = 'Mary Queen of Scots'"
    # If you find the movie, print out the details of the movie to the console
    pass


def task6():
    # Write code that deletes the item you added in task 4
    pass


def task7():
    # Write code that queries the movies database for all movies that contain the word Scotland in the title
    # Print out the details of any movies that you find
    # Use the following query: SELECT * FROM c WHERE CONTAINS(c.title, 'Scotland')
    pass


def task8():
    # Write code that updates the entry for movie 'The Enchanted Drawing' so that the cast list includes 'J. Stuart Blackton'
    pass

def task9():
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

def task10():
    # Write code that retrieves and prints the throughput of the movies container
    # If the throughput of the container is not already 500 RUs, then set it to 500 RUs
    pass

def task11():
    # Write code that creates a new container named StudiesContainer in the database you created in task 1
    pass

def task12():
    # Write code that deletes the StudiesContainer you just created
    pass

def task13():
    # Write code that deletes the database you created in task 1
    pass

task1()