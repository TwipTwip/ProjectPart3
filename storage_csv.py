import requests
import statistics

MOVIE_API = "http://www.omdbapi.com/?apikey=a27c1668&t="
API_KEY = "a27c1668"
import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, "r") as movie_info:
            length_check = movie_info.read()
        if len(length_check) == 0:
            print("No movies in file, please add a movie(s) first!")
            return "Empty"
        with open(self.file_path, "r") as movie_data:
            all_movies = csv.reader(movie_data)
            list_of_dict_movies = []
            for movie in all_movies:
                movie_dict = {"Title": movie[0],
                              "Year": movie[1],
                              "Rating": movie[2],
                              "Poster": movie[3]}
                list_of_dict_movies.append(movie_dict)
        return list_of_dict_movies

    def add_movie(self, title: str, year: int, rating: float, poster):
        new_movie = f'\n{title},{year},{rating},{poster}'
        with open(self.file_path, "r") as movie:
            len_check = movie.read()
            if len(len_check) == 0:
                movie.close()
                new_movie = f'{title},{year},{rating},{poster}'
                movies = new_movie
            else:
                with open(self.file_path, "r") as movie:
                    movies = movie.read()
        movie_info = movies + new_movie
        with open(self.file_path, "w") as add_movie:
            add_movie.write(movie_info)
            print(f"The movie '{title}' has successfully been added")
        return None

    def delete_movie(self, title):
        with open(self.file_path, "r") as del_movie:
            movies = csv.reader(del_movie)
            list_of_movies = []
            for movie in movies:
                list_of_movies.append(movie)
            index = -1
            for movie in list_of_movies:
                index += 1
                if title == movie[0]:
                    del (list_of_movies[index])
                    print(f"The movie '{title}' has successfully been deleted")
            counter = -1
            movie_info = ""
            for movie in list_of_movies:
                counter += 1
                if counter == 0:
                    movie_data = f'{movie[0]},{movie[1]},{movie[2]},{movie[3]}'
                    movie_info += movie_data
                else:
                    movie_data = f'\n{movie[0]},{movie[1]},{movie[2]},{movie[3]}'
                    movie_info += movie_data
            with open(self.file_path, "w") as delete:
                delete.write(movie_info)
                return None
            print("Couldn't find the movie entered in the file")
            return None

    def update_movie(self, title, rating):
        with open(self.file_path, "r") as update:
            movies = csv.reader(update)
            list_of_movies = []
            for movie in movies:
                list_of_movies.append(movie)
        for movie in list_of_movies:
            if title == movie[0]:
                movie[2] = rating
                print(f"The movie '{movie[0]}' has been updated with a new rating of {rating}")
        counter = -1
        movie_info = ""
        for movie in list_of_movies:
            counter += 1
            if counter == 0:
                movie_data = f'{movie[0]},{movie[1]},{movie[2]},{movie[3]}'
                movie_info += movie_data
            else:
                movie_data = f'\n{movie[0]},{movie[1]},{movie[2]},{movie[3]}'
                movie_info += movie_data
        with open(self.file_path, "w") as update:
            update.write(movie_info)
            return None
        print(f"The movie entered could not be found in the file")
        return None
