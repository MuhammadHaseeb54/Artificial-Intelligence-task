# Question 02
# Movie budget
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
new_movies = int(input("Enter the number how many new movies wants to add:"))
for _ in range(new_movies):
    name = input("Enter the new movie name: ")
    budget = int(input("Enter the movie budget: "))
    new_movie = (name, budget)
    movies.append(new_movie)

higher_budget_movies = []
total_budget = 0
for movie in movies:
    total_budget = total_budget + movie[1]
average_budget = int(total_budget // len (movies)) 
for movie in movies:
    if movie[1] > average_budget:
        higher_budget_movies.append(movie)
        over_budget_cost = movie[1] - average_budget
        print(f"{movie[0]} cost ${movie[1]:,} ${over_budget_cost:,}over budget.")
    print(f"There are {len(higher_budget_movies)} movies with over budget cost...\n")
print("Updated movies list is:", '\n', movies)