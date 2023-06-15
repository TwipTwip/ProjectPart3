MOVIE_API = "http://www.omdbapi.com/?apikey=a27c1668&t="
API_KEY = "a27c1668"
import requests
import statistics


class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """Lists the movies from the selected file"""
        movies = self._storage.list_movies()
        if movies == "Empty":
            return None
        for movie in movies:
            print(f"{movie['Title']}({movie['Year']}): Rating {movie['Rating']}")
        print("")
        return movies

    def _command_add_movie(self):
        """Adds a movie to the selected file"""
        SEARCH_URL = "http://www.omdbapi.com/?apikey=a27c1668&t="
        search_to_add_movie = input("Enter the name of the movie that you would like to add: ")
        url = f"{SEARCH_URL}{search_to_add_movie}"
        res = requests.get(url)
        if res.status_code == requests.codes.ok:
            returned_movie_info = res.json()
        if "Error" in returned_movie_info.keys():
            print("The movie you entered does not exist or it couldn't be found")
            return None
        self._storage.add_movie(returned_movie_info["Title"], returned_movie_info["Year"],
                                returned_movie_info["imdbRating"], returned_movie_info["Poster"])

    def _command_delete_movie(self):
        """Deletes a movie from the selected file"""
        del_movie = input("Enter the name of the movie that you would like to delete: ")
        self._storage.delete_movie(del_movie)

    def _command_update_movie(self):
        """Updates the rating of a movie"""
        movie_title = input("Enter the name of the movie that you would like to update: ")
        new_rating = input(f"Enter the new rating for the movie '{movie_title}': ")
        new_rating = float(new_rating)
        self._storage.update_movie(movie_title, new_rating)

    def _command_movie_stats(self):
        """Shows statistics of the movies from the selected file"""
        movies = self._storage.list_movies()

        average_rating = 0
        num_of_movies = 0
        for movie in movies:
            average_rating = average_rating + float(movie["Rating"])
            num_of_movies += 1
        average_rating = average_rating / num_of_movies
        average_rating = "{:.1f}".format(average_rating)
        print(f"Average rating: {average_rating}")

        median_rating = []
        for movie in movies:
            median_rating.append(float(movie["Rating"]))
        median_rating = (statistics.median(median_rating))
        print(f"Median rating: {median_rating}")

        all_movies = []
        for movie in movies:
            movie_rating = []
            movie_rating.append(float(movie["Rating"]))
            movie_rating.append(movie["Title"])
            movie_rating.append(movie["Year"])
            all_movies.append(movie_rating)
        all_movies = sorted(all_movies, reverse=True)
        best_movie = max(all_movies)
        worst_movie = min(all_movies)
        print(f"The best movie is {best_movie[1]}({best_movie[2]}) with a rating of {best_movie[0]}")
        print(f"The worst movie is {worst_movie[1]}({worst_movie[2]}) with a rating of {worst_movie[0]}")

    def _command_generate_website(self):
        """Generates a website from the selected file's movie information"""
        movie_info = self._storage.list_movies()
        output = ''
        for movie in movie_info:
            output += '<li>'
            output += '<div class="movie">'
            output += f'''<img class="movie-poster"
        src = "{movie["Poster"]}"/>'''
            output += f'<div class="movie-title">{movie["Title"]}</div>'
            output += f'<div class="movie-year">{movie["Year"]}</div>'
            output += '</div>'
            output += '</li>'
        with open("index_template.html", "r") as movies:
            website_movies = movies.read()
        website_movies = website_movies.replace(f"__TEMPLATE_MOVIE_GRID__", output)
        with open("index.html", "w") as website:
            website.write(website_movies)
            return website

    def run(self):
        """Makes the class run and lets the user select what function they want to run"""
        while True:
            print("""
        Menu:
        0. Exit
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats 
        6. Generate Website
        """)
            selection = int(input("Enter choice (0-6): "))
            print(" ")

            if selection == 0:
                print("Bye!")
                print(" ")
                break

            if selection == 1:
                self._command_list_movies()

            if selection == 2:
                self._command_add_movie()

            if selection == 3:
                self._command_delete_movie()

            if selection == 4:
                self._command_update_movie()

            if selection == 5:
                self._command_movie_stats()

            if selection == 6:
                self._command_generate_website()
                print("Website was generated successfully.")

            continue_app = input("Press the 'Enter' key to continue")
            if continue_app == "":
                continue
