import math  # импортируем модуль math

movies = [
    {"title": "The Dune Chronicles", 
     "year": 2021, 
     "genres": {"sci-fi", "drama"},
     "rating": 8.6, 
     "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", 
     "year": 2019, 
     "genres": {"comedy", "drama"},
     "rating": 7.1, 
     "duration_min": 98, 
     "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", 
     "year": 2016, 
     "genres": {"thriller", "drama"},
     "rating": 6.4, 
     "duration_min": 112, 
     "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", 
     "year": 2023, 
     "genres": {"sci-fi", "action"},
     "rating": 5.9, 
     "duration_min": 101, 
     "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", 
     "year": 2014, "genres": {"comedy"},
     "rating": 7.8, 
     "duration_min": 89, 
     "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", 
     "year": 2020, 
     "genres": {"thriller", "mystery"},
     "rating": 8.9, 
     "duration_min": 124, 
     "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", 
     "year": 2022, 
     "genres": {"drama"},
     "rating": 4.8, 
     "duration_min": 137, 
     "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", 
     "year": 2024, 
     "genres": {"sci-fi", "drama"},
     "rating": 9.2, 
     "duration_min": 118, 
     "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", 
     "year": 2011, 
     "genres": {"comedy"},
     "rating": 6.0, 
     "duration_min": 95, 
     "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", 
     "year": 2018, 
     "genres": {"action", "thriller"},
     "rating": 7.3, 
     "duration_min": 129, 
     "actors": ["P. Diaz", "T. Chalamet"]},
]

 # Этап 1. Разминка: переменные, числа, math
 
 # Возвращает среднюю оценку по каталогу, округленную до одного знака (round). 

def average_rating(movies):
    total_rating = 0  # создаем счетчик 
    for movie_rating in movies:
        total_rating += movie_rating['rating'] 
   
    avg_rating = total_rating / len(movies) # находим среднее значение
    return round(avg_rating, 1) # возвращаем значение 

# Возвращает кортеж (самый старый фильм в годах, самый новый фильм в годах, среднее), 
# где среднее округлено вверх до целого с помощью math.ceil.
    
def catalog_age_stats(movies, current_year=2026):
    ages = [] # создаем список, который будет хранить возраст всех фильмов
    for movie_age in movies:
        age = current_year - movie_age['year']
        ages.append(age) # добавляем вычисленный возраст фильма в созданный список

    oldest_movie = max(ages) # определяем самый старый фильм из списка
    newest_movie = min(ages) # определяем самый новый фильм из списка
    average_age = math.ceil(sum(ages) / len(ages)) 

    return (oldest_movie, newest_movie, average_age) 

# переводит минуты в формат "2ч 35м", 
# используя целочисленное деление и остаток от деления.

def duration_in_hours(minutes):
    hours = minutes // 60 # находим часы с целочисленным делением
    minut = minutes % 60 # находим минуты с остатком от деления
    return f'{hours}ч {minut}м' # возращаем результат в нужном виде

# Этап 2. Условия и match

# Возвращает категорию: "шедевр" (≥9), "хорошо" (7–8.9), 
# "средне" (5–6.9), "слабо" (<5). 

def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif 7 <= rating < 9:
        return 'хорошо'
    else:
        return 'средне' if 5 <= rating < 7 else 'слабо'
     

# возвращает метку "новые" (после 2020), 
# "недавние" (2015–2020) или "старые" (раньше 2015).

def decade_label(year):
    match year:
        case _ if year > 2020:
            return 'новые'
        case _ if 2015 <= year <= 2020:
            return 'недавние'
        case _ if year < 2015:
            return 'старые'

# Этап 3. Циклы.

# Выводим названия всех фильмов, которые НЕ относятся к жанру "comedy".

for films in movies:
    if 'comedy' in films['genres']: 
        continue
    print(films["title"])

# Найдем первый по порядку в списке фильм с рейтингом выше 9.0

i = 0

while i <= len(movies):
    movie = movies[i]
    if movie['rating'] >= 9.0:
        print(movie['title'])
        break
    i += 1 
else:
    print('Шедевров не найдено')

# Считает количество фильмов длиннее threshold минут

def count_long_movies(movies, threshold=120):
    count_films = 0
    for films in movies:
        if films['duration_min'] > threshold:
            count_films += 1
    return count_films

# Этап 4. Строки

# Приводим строку к формату Title Case (каждое слово с заглавной буквы) 
# без использования напрямую

def normalize_title(title):
    words = title.split()
    separation_string = []
    for word in words:
        new_word = word[0].upper() + word[1:]
        separation_string.append(new_word)
    return " ".join(separation_string)

# Превращаем нормализованное название в «слаг» вида the-quiet-algorithm

def make_slug(title):
    lower_slug = title.lower()
    slug = lower_slug.replace(' ', '-')
    return slug

# Возвращаем единую строку с описанием фильма

def format_report_line(movie):
    sorted_genres = sorted(movie['genres'])
    genres_string = ', '.join(str(film) for film in sorted_genres)
    duration_films = duration_in_hours(movie['duration_min']) 
    film_description = (
    f'{movie['title']} ({movie['year']}) - {movie['rating']}/10, '
    f'{duration_films}, жанры: {genres_string}'
    )
    return film_description

