class Movie:
    def __init__(self, title, rating):
        self._title = title
        self._rating = rating


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and new_title.strip().isalpha():
            self._title = new_title
        else:
            print("Please enter a valid title")

casa = Movie("Casa de papel", 5)
print(casa.title)
casa.title = "Casa de mama"
new = 'casa de mama'.strip("m")
print(new)
print(casa.title)