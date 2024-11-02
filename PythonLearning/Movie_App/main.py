# https://kivy.org/doc/stable/ Kivy Documentation
# Start for Binge Buddy Movie App
#import kivy as App
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.scrollview import ScrollView #if can find a way to have a good looking scrollview then will add back
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager

from tmdbv3api import TMDb, Movie, TV, Search

# Setup for the API connection
tmdb = TMDb()
tmdb.language = 'en'
tmdb.debug = True
# Change to environmental variable later for security of API Key 
tmdb.api_key = '74db8709512a3b71220e7584b2db98a7'

API_Read_Access_Token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NGRiODcwOTUxMmEzYjcxMjIwZTc1ODRiMmRiOThhNyIsInN1YiI6IjY1YTJmYTI0YTM0OTExMDEyZDA5ZTlmNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KptFKm98IE3FIMHPRbnHjOyQgO-Nh27QVuVmY84kVDg'

# Class to make a details page for the user
# Define a MovieDetailsScreen that inherits from the Screen
class MovieDetailsScreen(Screen):
    # Recieves the movie_name as a parameter and displays details for that movie or show
    def __init__(self, movie_id, **kwargs):
        super(MovieDetailsScreen, self).__init__(**kwargs)
        self.movie_id = movie_id
        self.layout_build()

    def layout_build(self):
        layout = ScrollView()
        details_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        details_layout.bind(minimum_height=details_layout.setter('height'))

        # Fetch details based on movie_id
        details = self.fetch_movie_details()

        if details:
            for key, value in details.items():
                detail_box = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=dp(40))
                detail_label = Label(text=f"{key}:", size_hint_x=0.3, halign='left', valign='top')
                detail_text = Label(text=str(value), size_hint_x=0.7, halign='left', valign='top')
                detail_box.add_widget(detail_label)
                detail_box.add_widget(detail_text)
                details_layout.add_widget(detail_box)

        back_button = Button(text="Go Back", size_hint=(1, None), height=40)
        back_button.bind(on_press=self.go_back)

        details_layout.add_widget(back_button)
        layout.add_widget(details_layout)
        self.add_widget(layout)

    def fetch_movie_details(self):
        movie = Movie()
        details = {}
        try:
            movie_details = movie.details(self.movie_id)
            if movie_details:
                details['Title'] = movie_details.title
                details['Overview'] = movie_details.overview
                details['Release Date'] = movie_details.release_date
                details['Popularity'] = movie_details.popularity
                details['Vote Average'] = movie_details.vote_average
                # Add more details as needed
            else:
                print("No movie details found")
        except Exception as e:
            print(f"Error fetching movie details: {e}")
            return None

        return details

    def go_back(self, instance):
        self.manager.current = "main"

# Main Class for the Movie App
class MoviePage(Widget):
    pass

class MovieApp(App):
    '''
    classdocs
    '''
    # def build(self):
    #     layout_instance = Layout()
    #     layout = layout_instance.layoutBuild()  # Call layoutBuild on the instance
    #     return layout
    # Created a screenManager to manage differents screens
    def build(self):
        self.layout_instance = Layout(self)
        self.screen_manager = ScreenManager()
        main_screen = self.layout_instance.layoutBuild()
        self.main_screen = Screen(name="main")
        self.main_screen.add_widget(main_screen)
        self.screen_manager.add_widget(self.main_screen)
        return self.screen_manager

    # def show_movie_details(self, movie_name):
        # details_screen = MovieDetailsScreen(movie_name)
        # self.screen_manager.add_widget(details_screen)
        # self.screen_manager.current = "main"  # Switch to the main screen
        # self.screen_manager.current = details_screen.name  # Switch to the details screen

    def show_movie_details(self, movie_id):
        # Remove existing details screen if any
        if "details" in self.screen_manager.screen_names:
            self.screen_manager.remove_widget(self.screen_manager.get_screen("details"))
        
        details_screen = MovieDetailsScreen(name="details", movie_id=movie_id)
        self.screen_manager.add_widget(details_screen)
        self.screen_manager.current = "details"  # Switch to the details screen


class Layout():
    # def layoutBuild(self):
    #     main_layout = BoxLayout(orientation='vertical')
        
    #     inner_layout = BoxLayout(orientation='vertical')  # Create a layout to hold buttons
        
    #     search_box = TextInput(hint_text="Search for a show")
    #     search_box.bind(on_text_validate=lambda query: self.search_and_add(query, inner_layout))
    #     homepage = MoviePage()
    #     inner_layout.add_widget(homepage)

    #     movie = Movie()
    #     popular = movie.popular()
    #     for show in popular:
    #         button = Button(text=show.title)
    #         inner_layout.add_widget(button)  # Add buttons to the inner layout

    #     clearbtn = Button(text='Add Show')
    #     inner_layout.add_widget(clearbtn)

    #     main_layout.add_widget(inner_layout)  # Add the inner layout directly to the main layout
    #     return main_layout

    # def search_and_add(self, query, layout):
    #     search_results = tmdb.Search().movie(query=query)
    #     for result in search_results:
    #         show_button = Button(text=result.title)
    #         show_button.bind(on_press=self.add_show_to_main_page)
    #         layout.add_widget(show_button)

    # def add_show_to_main_page(self, instance):
    #     # Implement what happens when a show is added to the main page
    #     pass

    def __init__(self, app):
        self.search = Search()
        self.app = app

    def layoutBuild(self):
        main_layout = BoxLayout(orientation='vertical')

        # Search box and button
        search_box = TextInput(hint_text="Search for a movie or TV show", size_hint=(1, 0.1))
        search_button = Button(text="Search", size_hint=(1, 0.1))
        search_button.bind(on_press=lambda instance: self.search_and_add(search_box.text))

        # Scrollable grid layout for displaying search results
        self.grid_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.scroll_view = ScrollView(size_hint=(1, 0.8))
        self.scroll_view.add_widget(self.grid_layout)

        main_layout.add_widget(search_box)
        main_layout.add_widget(search_button)
        main_layout.add_widget(self.scroll_view)

        return main_layout

    def search_and_add(self, query):
        self.grid_layout.clear_widgets()  # Clear existing search results
        
        # Search for movies
        movie_results = self.search_movie(query)
        for result in movie_results:
            button = Button(text=f"Movie: {result.title}", size_hint_y=None, height=40)
            button.bind(on_press=lambda instance, id=result.id, title=result.title: self.app.show_movie_details(id))
            self.grid_layout.add_widget(button)
        
        # Search for TV shows
        tv_results = self.search_tv(query)
        for result in tv_results:
            button = Button(text=f"TV Show: {result.name}", size_hint_y=None, height=40)
            button.bind(on_press=lambda instance, id=result.id, name=result.name: self.app.show_movie_details(name))
            self.grid_layout.add_widget(button)

    def search_movie(self, query):
        search_results = self.search.movies(query)
        return search_results

    def search_tv(self, query):
        tv_results = self.search.tv_shows(query)
        return tv_results



if __name__ == '__main__':
    MovieApp().run()
