#**Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.

class moviedetails:

	def __init__(self,movie,artistname,year_of_release,ratings):
		self.movie=movie
		self.artistname=artistname
		self.year_of_release=year_of_release
		self.ratings=ratings
		
	def display(self):
		print("movie:",self.movie)
		print("artistname:",self.artistname)
		print("year_of_release:",self.year_of_release)
		print("ratings:",self.ratings)
		print("")
		
	def update(self,movie,artistname,year_of_release,ratings):
		self.movie=movie
		self.artistname=artistname
		self.year_of_release=year_of_release
		self.ratings=ratings
	
		
a=moviedetails(input("enter the new movie:"),input("enter the artistname:"),input("enter the year_of_release:"),input("enter the ratings"))
a.display()
a.update(input("enter the new movie:"),input("enter the artistname:"),input("enter the year_of_release:"),input("enter the ratings"))
a.display()
