from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """Lists all of the movies that are saved"""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the list"""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Deletes a movie from the list of movies"""
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """Updates/changes the rating of the selected movie,
        kind of a useless funciton because the rating is now collected
        from an API"""
        pass
