"""
 * Date: 2023년 11월 2일
 * Author: 박병규, 이대규, 조성진
 * Description: 일기장
 * Version: 2.0
 """
import time
from datetime import datetime

def create_diary(_id, _title, _weather, _date, _content, _diary_list):
    _diary_list.append(dict(
        diary_id=_id,
        diary_title=_title,
        diary_weather=_weather,
        diary_date=_date,
        diary_content=_content
    ))
    return _diary_list

def append_to_diary(_id, _content, _diary_list):
    for diary in _diary_list:
        if diary["diary_id"] == _id:
            diary["diary_content"] += "\n" + _content
            return True, _diary_list
    return False, None

def read_diary(_id, _diary_list):
    for diary in _diary_list:
        if diary["diary_id"] != _id:
            continue
        return True, diary
    return False, None

def update_diary(_id, _content, _diary_list):
    is_update = False
    for idx, diary in enumerate(_diary_list):
        if diary["diary_id"] == _id:
            diary["diary_content"] = _content
            is_update = True
            break
    if is_update:
        return True, _diary_list
    return False, None

def delete_diary(_id, _diary_list):
    for idx, diary in enumerate(_diary_list):
        if diary["diary_id"] != _id:
            continue
        del _diary_list[idx]
        return True, _diary_list
    return False, None

def save_diary_to_file(filename, diary_list):
    with open(filename, 'w') as file:
        for diary in diary_list:
            file.write(f'{diary["diary_id"]}|{diary["diary_title"]}|{diary["diary_weather"]}|{diary["diary_date"]}|{diary["diary_content"]}\n')

def load_diary_from_file(filename):
    diary_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 5:
                    _id, _title, _weather, _date, _content = parts
                    _id = int(_id)
                    diary_list.append(dict(
                        diary_id=_id,
                        diary_title=_title,
                        diary_weather=_weather,
                        diary_date=_date,
                        diary_content=_content
                    ))
    except FileNotFoundError:
        diary_list = []
    return diary_list

# if __name__ == '__main__':
#     def main():
#         diary_list = load_diary_from_file('diary.txt')
#         if not diary_list:
#             idx = 0
#         else:
#             idx = max(diary["diary_id"] for diary in diary_list) + 1
#
#         while True:
#             print("=" * 30 + "\n",
#                   "일기 프로그램\n",
#                   "=" * 30 + "\n",
#                   "0. 일기 목록보기\n",
#                   "1. 일기 작성하기\n",
#                   "2. 일기 불러오기\n",
#                   "3. 일기 수정하기\n",
#                   "4. 일기 삭제하기\n",
#                   "5. 일기 이어쓰기\n",
#                   "6. 프로그램 종료",
#                   sep=""
#                   )
#             cmd = int(input("번호를 선택하세요: "))
#             if cmd == 0:
#                 print("|> 일기 목록")
#                 for diary in diary_list:
#                     print(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')
#             elif cmd == 1:
#                 title = input("|> 일기 제목을 입력하세요: ")
#                 weather = input("|> 날씨를 입력하세요: ")
#                 content = input("|> 일기 내용을 입력하세요: ")
#                 date = datetime.now().strftime('%Y-%m-%d')
#                 diary_list = create_diary(idx, title, weather, date, content, diary_list)
#                 idx += 1
#                 save_diary_to_file('diary.txt', diary_list)
#             elif cmd == 2:
#                 d_id = int(input("|> 불러올 일기 ID를 입력하세요: "))
#                 res, diary = read_diary(d_id, diary_list)
#                 if res:
#                     print("|> 일기를 성공적으로 불러왔습니다.")
#                     print(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')
#                     print(f'게시일: {diary["diary_date"]}')
#                     print(f'날씨: {diary["diary_weather"]}')
#                     print(f'내용: {diary["diary_content"]}')
#                 else:
#                     print("|> 일기를 불러오지 못했습니다.")
#             elif cmd == 3:
#                 d_id = int(input("|> 수정할 일기 ID를 입력하세요: "))
#                 content = input("|> 일기 내용을 입력하세요: ")
#                 res, _diary_list = update_diary(d_id, content, diary_list)
#                 if res:
#                     print("|> 수정에 성공했습니다.")
#                     diary_list = _diary_list
#                     save_diary_to_file('diary.txt', diary_list)
#                 else:
#                     print("|> 수정에 실패했습니다.")
#             elif cmd == 4:
#                 d_id = int(input("|> 삭제할 일기 ID를 입력하세요: "))
#                 res, _diary_list = delete_diary(d_id, diary_list)
#                 if res:
#                     print("|> 삭제에 성공했습니다.")
#                     diary_list = _diary_list
#                     save_diary_to_file('diary.txt', diary_list)
#                 else:
#                     print("|> 삭제에 실패했습니다.")
#             elif cmd == 5:
#                 d_id = int(input("|> 이어쓸 일기 ID를 입력하세요: "))
#                 content = input("|> 이어쓸 내용을 입력하세요: ")
#                 res, _diary_list = append_to_diary(d_id, content, diary_list)
#                 if res:
#                     print("|> 이어쓰기에 성공했습니다.")
#                     diary_list = _diary_list
#                     save_diary_to_file('diary.txt', diary_list)
#                 else:
#                     print("|> 이어쓰기에 실패했습니다.")
#             elif cmd == 6:
#                 break
#             print()
#     main()