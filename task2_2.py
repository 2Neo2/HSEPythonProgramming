# Task 1.
ids = {}

for i in range(1, 4):
    user_input = input(f"Введите координаты через пробел для user{i}: ")
    geo_tags = user_input.split(' ')
    ids[f'user{i}'] = geo_tags

unique_geo_tags = set()

for geo_tags in ids.values():
    unique_geo_tags.update(geo_tags)

print(unique_geo_tags)

#==============================
# Task 2.

count_word_info = {}

for i in range(1, 12):
    user_input = input(f"Введите запрос{i}: ")
    geo_tags = user_input.split(' ')

    count_word_info[len(geo_tags)] = count_word_info.get(len(geo_tags), 0)
    count_word_info[len(geo_tags)] += 1

for count_words, value in count_word_info.items():
    percent = (value / 11) * 100
    print(f"Поисковых запросов, содержащих {count_words} слов(а): {percent:.2f}%")
