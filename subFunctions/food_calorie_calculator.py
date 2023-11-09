"""
 * Date: 2023년 11월 8일
 * Author: 김성모, 이현우
 * Minor Author : 조성진
 * Description: 칼로리 계산 기능 연동
 * Version: 1.0
"""
from PhysicalDiary.DB.food_db import FoodDB
from PhysicalDiary.DB.sports_db import SportsDB

def calculate_calories(diary_content):
    total_calories = 0

    for food, calories in FoodDB.food_calories.items():
        if food in diary_content:
            total_calories += calories * diary_content.count(food)

    for exercise, calories_burned in SportsDB.sports_calories.items():
        if exercise in diary_content:
            total_calories -= calories_burned * diary_content.count(exercise)

    return total_calories
