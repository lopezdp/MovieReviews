import webbrowser

# Parent Class for all Videos
class Video():
    # Constructor - Commonalities of all video types
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Parent Class Methods
    def show_trailer(self):
        # Method uses webbrowser module to open a web browser
        # window using a url
        webbrowser.open(self.trailer_youtube_url)

# Child Class of Video - Movie()
class Movie(Video):
    # Class Decription & Documentation
    """This class provides a way to store movie related information"""
    
    # Static (Class) Variables
    # Constant array (Constants in Caps)
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    # Constructor
    def __init__(self, movie_title, storyline, poster_img,
                trailer_url, rating):
        # To set the variable with an index of the Class Variable array
        # Programmer must also use the self pointer to refer to the
        # Static (Class) variable array!!
        self.movie_rating = self.VALID_RATINGS[rating]

        # Inherit from Parent Class - Video()
        Video.__init__(self, movie_title, storyline, poster_img, trailer_url)
        
        
    
        

    
        
        
        
    
    
