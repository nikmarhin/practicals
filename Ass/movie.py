"""
CP1404 - Programming 2
Assignment 2 - Movie Class
Student: Nik Marhin
"""


class Movie:
    """Movie Class"""

    def __int__(self, title="", year=0, category="", watched_status="u"):
        """Initialise a Movie object"""
        self.title = title
        self.year = year
        self.category = category
        self.watched = watched_status

    def __str__(self):
        """Return string representation of data in a City"""
        return f"{self.title}, from year {self.year} is a {self.category}"

    def is_watched(self):
        """Mark a movie as watched"""
        return self.watched_status == "w"

    def is_unwatched(self):
        """Mark a movie as unwatched"""
        return self.watched_status == "u"
