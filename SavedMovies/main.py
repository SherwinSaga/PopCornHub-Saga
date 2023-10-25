import tkinter as tk
from tkinter import ttk

class MovieManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Manager")
        self.root.geometry("800x600")  # Set the window size

        #tabs for Favorite, Watchlist, and Watched
        self.notebook = ttk.Notebook(root)
        self.favorite_tab = tk.Frame(self.notebook)
        self.watchlist_tab = tk.Frame(self.notebook)
        self.watched_tab = tk.Frame(self.notebook)
        self.notebook.add(self.favorite_tab, text='Favorites')
        self.notebook.add(self.watchlist_tab, text='Watchlist')
        self.notebook.add(self.watched_tab, text='Watched')
        self.notebook.pack(fill='both', expand=True)

        #buttons and lists
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TListbox', font=('Helvetica', 14))

        # Favorites Tab
        self.favorite_list = tk.Listbox(self.favorite_tab, selectbackground='gold', selectmode=tk.SINGLE)
        self.favorite_list.pack(fill='both', expand=True, padx=20, pady=20)
        self.favorite_button = ttk.Button(self.favorite_tab, text='Add to Favorites')
        self.favorite_button.pack(pady=10)

        # Static Elements for Favorites Tab
        favorite_title_label = tk.Label(self.favorite_tab, text='Your Favorite Movies', font=('Helvetica', 16, 'bold'))
        favorite_title_label.pack(pady=10)

        # Sample Favorites
        sample_favorites = [
            "Movie 1",
            "Movie 2",
            "Movie 3",
        ]
        for movie in sample_favorites:
            self.favorite_list.insert(tk.END, movie)


        #watchlist tab
        self.watchlist_list = tk.Listbox(self.watchlist_tab, selectbackground='lightblue', selectmode=tk.SINGLE)
        self.watchlist_list.pack(fill='both', expand=True, padx=20, pady=20)
        self.watchlist_button = ttk.Button(self.watchlist_tab, text='Add to Watchlist')
        self.watchlist_button.pack(pady=10)


        #watched tab
        self.watched_list = tk.Listbox(self.watched_tab, selectbackground='lightgreen', selectmode=tk.SINGLE)
        self.watched_list.pack(fill='both', expand=True, padx=20, pady=20)
        self.watched_button = ttk.Button(self.watched_tab, text='Mark as Watched')
        self.watched_button.pack(pady=10)

        # You can bind the buttons to functions that add, remove, or manage movies

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieManagerApp(root)
    root.mainloop()
