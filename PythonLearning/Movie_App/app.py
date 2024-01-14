"""Movie App with tmdbv3Api to track TV Shows, Movies, and Anime"""
import tkinter as tk
import tmdbv3api as TMDb

# Connection to teh tmdb api with the API key that was given when registered
tmdb = TMDb()
tmdb.api_key = "YOUR_API_KEY"  # Replace with your actual API key

# Tkinter UI that titles the GUI as Watch Tracker
root = tk.Tk()
root.title("Binge Buddy")
# Add UI elements (labels, entry fields, buttons, etc.)
# as needed for search and display functionality