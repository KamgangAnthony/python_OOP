class Book:

	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self.author = author
		self._num_pages = num_pages
		self._ISBN = ISBN
		self._publisher = publisher

the_book = Book("The 5am club", "Robin Sharma", "255", "I don't know its ISBN","Robin Sharma")
print(the_book._num_pages)
