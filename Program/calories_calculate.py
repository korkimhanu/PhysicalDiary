# 음식과 칼로리 정보를 포함한 딕셔너리 생성

# 운동과 소모 칼로리 정보를 포함한 딕셔너리 생성
from DB.food_db import FoodDB
from DB.sport_db import SportDB

total_calories = 0

while True:
    diary_entry = input("음식 또는 운동과 함께 일기를 작성하세요 (종료하려면 '종료'를 입력하세요): ")

    if diary_entry == "종료":
        break

    entry_calories = 0

    # 음식과 칼로리 정보 찾기
    for food, calories in FoodDB.food_calories.items():
        if food in diary_entry:
            entry_calories += calories * diary_entry.count(food)
            diary_entry = diary_entry.replace(food, f"{food}({calories}kcal)", diary_entry.count(food))

    # 운동과 소모 칼로리 정보 찾기
    for exercise, calories_burned in SportDB.sport_calories.items():
        if exercise in diary_entry:
            entry_calories -= calories_burned * diary_entry.count(exercise)
            diary_entry = diary_entry.replace(exercise, f"{exercise}(-{calories_burned}kcal)",
                                              diary_entry.count(exercise))

    total_calories += entry_calories
    print(f"일기에 기록된 총 칼로리: {entry_calories}kcal")
    print(f"일기 내용: {diary_entry}")

print(f"총 칼로리: {total_calories}kcal")