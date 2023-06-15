from istorage import IStorage
import json
import requests
import statistics

MOVIE_API = "http://www.omdbapi.com/?apikey=a27c1668&t="
API_KEY = "a27c1668"


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        with open(self.file_path, "r") as movie_info:
            length_check = movie_info.read()
            if len(length_check) == 0:
                print("No movies in file, please add a movie(s) first!")
                return "Empty"
        with open(self.file_path, "r") as movie_data:
            all_movies = json.loads(movie_data.read())
        all_movies = list(all_movies)
        return all_movies

    def add_movie(self, title: str, year: int, rating: float, poster):
        new_movie = {"Title": title,
                     "Year": year,
                     "Rating": rating,
                     "Poster": poster}
        with open(self.file_path, "r") as movie:
            len_check = movie.read()
            if len(len_check) == 0:
                movie.close()
                movies = []
                movies.append(new_movie)
            else:
                with open(self.file_path, "r") as movie:
                    movies = json.loads(movie.read())
                movies = list(movies)
                movies.append(new_movie)
        with open(self.file_path, "w") as add_movie:
            add_movie.write(json.dumps(movies))
            print(f"The movie '{title}' has successfully been added")
        return None

    def delete_movie(self, title):
        with open(self.file_path, "r") as del_movie:
            movies = json.loads(del_movie.read())
            movies = list(movies)
            index = -1
            for movie in movies:
                index += 1
                if title == movie["Title"]:
                    del (movies[index])
                    print(f"The movie '{title}' has successfully been deleted")
                    with open(self.file_path, "w") as delete:
                        delete.write(json.dumps(movies))
                    return None
            print("Couldn't find the movie entered in the file")
            return None

    def update_movie(self, title, rating):
        with open(self.file_path, "r") as update:
            movies = json.loads(update.read())
            movies = list(movies)
            for movie in movies:
                if title == movie["Title"]:
                    movie["Rating"] = rating
                    print(f"The movie '{title}' has been updated with a new rating of {rating}")
                    with open(self.file_path, "w") as update:
                        update.write(json.dumps(movies))
                    return None
            print(f"The movie entered could not be found in the file")
            return None
