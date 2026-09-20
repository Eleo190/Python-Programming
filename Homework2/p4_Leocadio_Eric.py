#PROBLEM 4
import csv

def display_top_collaborations(top_casts_file, top_rated_file):
    try:
        with open(top_casts_file, 'r', encoding='utf-8') as top_casts:
            with open(top_rated_file, 'r', encoding='utf-8') as top_rated:
                collabs = {}
                cast_reader = csv.reader(top_casts)
                rated_reader = csv.DictReader(top_rated, skipinitialspace=True)
                movie_list = set()
                for movie in rated_reader:
                    #make a set of all movies in the top 250 to make checking if each movie in top_casts is in top_rated simpler
                    movie_list.add(movie['Title'])
                for row in cast_reader:
                    if row[0] in movie_list:
                        #check if the movie title is in the list of 250 movies, then set director and actor variables to make dictionary and ease of reading
                        director = row[2]
                        for actor in row[3:8]:
                            if (director, actor) in collabs:
                                #save director actor pairs as tuple to be the key in collabs dict and count occurences
                                collabs[(director, actor)] += 1
                            else: collabs[(director, actor)] = 1
                collabs_list = [(director, actor, number) for (director, actor), number in collabs.items()]
                collabs_list = tuple(sorted(collabs_list, key=lambda item:item[2], reverse=True))
                print(collabs_list)
    except IOError as err:
        print(f"An Error Occured!: {err}")
        raise

def display_top_actors(top_casts_file, gross_file):
    try:
        with open(top_casts_file, 'r', encoding='utf-8') as top_casts:
            with open(gross_file, 'r', encoding='utf-8') as gross:
                grossing_list = {}
                cast_reader = csv.reader(top_casts)
                gross_reader = csv.reader(gross)
                movie_list = {}
                #skip header line
                next(gross_reader)
                for movie in gross_reader:
                    #make a dict of all movies in the top 250 to make getting money and movies easier
                    movie_list[movie[1]] = int(movie[3])
                for movie in cast_reader:
                    if movie[0] in movie_list:
                        for actor in movie[3:8]:
                            if actor in grossing_list:
                                grossing_list[actor] += movie_list[movie[0]]
                            else: grossing_list[actor] = movie_list[movie[0]]
                grossing_list = sorted(grossing_list.items(), key=lambda item:item[1], reverse=True)
                print(grossing_list)
    except IOError as err:
        print(f"An error has occurred! {err}")
        raise

def main():
    display_top_collaborations('Homework2/imdb-top-casts.csv', 'Homework2/imdb-top-rated.csv')
    display_top_actors('Homework2/imdb-top-casts.csv', 'Homework2/imdb-top-grossing.csv')
    print("ERIC LEOCADIO Z2312790")
if __name__ == "__main__":
    main()