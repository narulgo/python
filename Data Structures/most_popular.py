def most_popular(movies):
    latest_time = None
    name_temp = None
    for movie in movies:
        movie_time =  movie['time']
        if latest_time is None or movie_time > latest_time:
            latest_time = movie_time
            name_temp = movie
    return name_temp

movies = [{'theatre': 'Bekmambetov Cinema', 'name': 'Девятая', 'time': '00:50'}, {'theatre': 'Bekmambetov Cinema', 'name': 'Доктор Сон', 'time': '00:50'}, {'theatre': 'Bekmambetov Cinema', 'name': 'Зеркала', 'time': '00:45'}, {'theatre': 'Chaplin (ADK)', 'name': 'Аким', 'time': '00:10'}, {'theatre': 'Chaplin (ADK)', 'name': 'Во всё тяжкое', 'time': '00:15'}, {'theatre': 'Chaplin (ADK)', 'name': 'Семейка Аддамс','time': '00:20'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Во всё тяжкое', 'time': '00:00'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Девятая', 'time': '00:10'}, {'theatre': 'Chaplin (Mega Park)', 'name': 'Райские холмы', 'time': '00:10'}, {'theatre': 'Cinema Towers', 'name': 'Девятая', 'time': '00:00'}, {'theatre': 'Cinema Towers', 'name': 'Доктор Сон', 'time': '00:25'}]
print(most_popular(movies))

