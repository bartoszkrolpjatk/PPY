from collections import defaultdict

def create_actor_films_dict(film_actors_dict):
    res = defaultdict(list)
    for film, actors in film_actors_dict.items():
        for actor in actors:
            res[actor].append(film)
    return res

films = dict(a=[1, 3, 5], b=[2, 1, 4], c=[5, 2], d=[3, 4, 6],
             e=[1], f=[3, 4, 5], g=[1, 7], h=[7, 6])

actor_films_dict = create_actor_films_dict(films)
#sort by films length desc then by actor id asc
sorted_actor_films = sorted(actor_films_dict.items(), key=lambda item: (len(item[1]), -item[0]), reverse=True)

for key, val in sorted_actor_films:
    print(f"{key} -> {val}")
