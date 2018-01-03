import webbrowser



class Movie():
    def __init__(self,title,storyline,poster_url,trailer_url,):
        self.title = title
        self.story = storyline
        self.poster = poster_url
        self.trailer = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)
