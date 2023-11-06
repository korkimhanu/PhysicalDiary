"""
 * Date: 2023년 11월 4일
 * Author: 김성모, 이현우
 * Minor Author : 박병규, 이대규, 조성진
 * Description: 칼로리 계산
 * Version: 1.0
"""

import os
from DB.food_db import FoodDB
from DB.sports_db import SportsDB

def read_diary_content(diary_file_path):
    with open(diary_file_path, 'r') as file:
        diary_entries = file.readlines()
    return [entry.split('|')[4] for entry in diary_entries]

total_calories = 0

script_directory = os.path.dirname(os.path.abspath(__file__))
diary_file_path = os.path.join(script_directory, '..', 'DB', 'diary_data.txt')

diary_content_list = read_diary_content(diary_file_path)

for diary_content in diary_content_list:
    entry_calories = 0

    for food, calories in FoodDB.food_calories.items():
        if food in diary_content:
            entry_calories += calories * diary_content.count(food)
            diary_content = diary_content.replace(food, f"{food}({calories}kcal)", diary_content.count(food))

    for exercise, calories_burned in SportsDB.sports_calories.items():
        if exercise in diary_content:
            entry_calories -= calories_burned * diary_content.count(exercise)
            diary_content = diary_content.replace(exercise, f"{exercise}(-{calories_burned}kcal)", diary_content.count(exercise))

    total_calories += entry_calories
    print(f"일기에 기록된 총 칼로리: {entry_calories}kcal")
    print(f"일기 내용: {diary_content}")

print(f"총 칼로리: {total_calories}kcal")