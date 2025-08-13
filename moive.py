import numpy as np

# Movie data
movies = [
    {"Title": "The Legend of Maula Jatt", "Genre": "Action, Drama", "Year": 2022, "Rating": 8.5, "Votes": 11000},
    {"Title": "Bol", "Genre": "Drama", "Year": 2011, "Rating": 8.2, "Votes": 9300},
    {"Title": "In the Name of God", "Genre": "Drama", "Year": 2007, "Rating": 8.3, "Votes": 9700},
    {"Title": "Manto", "Genre": "Biography, Drama", "Year": 2015, "Rating": 8.2, "Votes": 1300},
    {"Title": "Parwaaz Hai Junoon", "Genre": "Action, Romance", "Year": 2018, "Rating": 7.5, "Votes": 1800}
]

# Extract ratings and votes into NumPy arrays
ratings = np.array([movie["Rating"] for movie in movies])
votes = np.array([movie["Votes"] for movie in movies])

# 1. Average rating
avg_rating = np.mean(ratings)
print(f"Average Movie Rating: {avg_rating:.2f}")

# 2. Highest rated movie
max_rating = np.max(ratings)
highest_movie = [m for m in movies if m["Rating"] == max_rating][0]
print(f"Highest Rated Movie: {highest_movie['Title']} ({highest_movie['Rating']})")

# 3. Most popular movie by votes
max_votes = np.max(votes)
popular_movie = [m for m in movies if m["Votes"] == max_votes][0]
print(f"Most Popular Movie: {popular_movie['Title']} ({popular_movie['Votes']} votes)")

# 4. Rating standard deviation
std_dev_rating = np.std(ratings)
print(f"Rating Standard Deviation: {std_dev_rating:.2f}")
