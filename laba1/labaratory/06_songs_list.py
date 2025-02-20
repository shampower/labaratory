# -*- coding: utf-8 -*-

# Список песен группы Depeche Mode со временем звучания
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.90],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Время звучания песен 'Halo', 'Enjoy the Silence' и 'Clean'
halo_time = next(song[1] for song in violator_songs_list if song[0] == 'Halo')
enjoy_the_silence_time = next(song[1] for song in violator_songs_list if song[0] == 'Enjoy the Silence')
clean_time = next(song[1] for song in violator_songs_list if song[0] == 'Clean')
total_time_list = halo_time + enjoy_the_silence_time + clean_time
print(f"Три песни звучат {total_time_list:.2f} минут")

# Словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.60,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Время звучания песен 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
sweetest_perfection_time = violator_songs_dict.get('Sweetest Perfection')
policy_of_truth_time = violator_songs_dict.get('Policy of Truth')
blue_dress_time = violator_songs_dict.get('Blue Dress')
total_time_dict = sweetest_perfection_time + policy_of_truth_time + blue_dress_time
print(f"А другие три песни звучат {total_time_dict:.2f} минут")