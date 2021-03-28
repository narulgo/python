def most_popular(movies):
    result = {}
    movie_temp = None
    for movie in movies:
        movie_name = movie['name']
        if movie_name not in result:
            result[movie_name] = 1
        else:
            result[movie_name] += 1
    maximum = 0
    for movie_name, movie_count in result.items():
        if movie_count > maximum:
            maximum = movie_count
            movie_temp = movie_name
    return movie_temp


movies = [{'theatre': 'Bekmambetov Cinema', 'name': 'Девятая', 'time': '00:50'}, {'theatre': 'Bekmambetov Cinema', 'name': 'Доктор Сон', 'time': '00:50'}, {'theatre': 'Bekmambetov Cinema', 'name': 'Зеркала', 'time': '00:45'}, {'theatre': 'Chaplin (ADK)', 'name': 'Аким', 'time': '00:10'}, {'theatre': 'Chaplin (ADK)', 'name': 'Во всё тяжкое', 'time': '00:15'}, {'theatre': 'Chaplin (ADK)', 'name': 'Семейка Аддамс','time': '00:20'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Во всё тяжкое', 'time': '00:00'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Девятая', 'time': '00:10'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Райские холмы', 'time': '00:10'}, {'theatre': 'Cinema Towers', 'name': 'Девятая', 'time': '00:00'}, {'theatre': 'Cinema Towers', 'name': 'Доктор Сон', 'time': '00:25'}]
print(most_popular(movies))
