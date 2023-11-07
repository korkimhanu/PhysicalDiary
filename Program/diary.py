"""
 * Date: 2023년 11월 2일
 * Author: 박병규, 이대규, 조성진
 * Description: 일기장
 * Version: 3.0
"""
import os
import time
from datetime import datetime

class DiaryManager:
    def __init__(self):
        self.diary_list = []
        self.data_file = os.path.join(os.path.dirname(__file__), '..', 'DB', 'diary_data.txt')

    def load_diary_from_file(self):
        try:
            with open(self.data_file, 'r',encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 5:
                        _id, _title, _weather, _date, _content = parts
                        _id = int(_id)
                        self.diary_list.append(dict(
                            diary_id=_id,
                            diary_title=_title,
                            diary_weather=_weather,
                            diary_date=_date,
                            diary_content=_content
                        ))
        except FileNotFoundError:
            self.diary_list = []

    def save_diary_to_file(self):
        with open(self.data_file, 'w') as file:
            for diary in self.diary_list:
                file.write(f'{diary["diary_id"]}|{diary["diary_title"]}|{diary["diary_weather"]}|{diary["diary_date"]}|{diary["diary_content"]}\n')

    def create_diary(self, _title, _weather, _content):
        if not self.diary_list:
            idx = 0
        else:
            idx = max(diary["diary_id"] for diary in self.diary_list) + 1
        date = datetime.now().strftime('%Y-%m-%d')
        self.diary_list.append(dict(
            diary_id=idx,
            diary_title=_title,
            diary_weather=_weather,
            diary_date=date,
            diary_content=_content
        ))
        self.save_diary_to_file()

    def append_to_diary(self, _id, _content):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                diary["diary_content"] += "\n" + _content
                self.save_diary_to_file()
                return True
        return False

    def read_diary(self, _id):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                return diary
        return None

    def update_diary(self, _id, _content):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                diary["diary_content"] = _content
                self.save_diary_to_file()
                return True
        return False

    def delete_diary(self, _id):
        for diary in self.diary_list:
            if diary["diary_id"] == _id:
                self.diary_list.remove(diary)
                self.save_diary_to_file()
                return True
        return False

if __name__ == '__main__':
    diary_manager = DiaryManager()
    diary_manager.load_diary_from_file()

    while True:
        print("=" * 30 + "\n",
              "일기 프로그램\n",
              "=" * 30 + "\n",
              "0. 일기 목록보기\n",
              "1. 일기 작성하기\n",
              "2. 일기 불러오기\n",
              "3. 일기 수정하기\n",
              "4. 일기 삭제하기\n",
              "5. 일기 이어쓰기\n",
              "6. 프로그램 종료",
              sep=""
              )
        cmd = int(input("번호를 선택하세요: "))
        if cmd == 0:
            print("|> 일기 목록")
            for diary in diary_manager.diary_list:
                print(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')
        elif cmd == 1:
            title = input("|> 일기 제목을 입력하세요: ")
            weather = input("|> 날씨를 입력하세요: ")
            content = input("|> 일기 내용을 입력하세요: ")
            diary_manager.create_diary(title, weather, content)
        elif cmd == 2:
            d_id = int(input("|> 불러올 일기 ID를 입력하세요: "))
            diary = diary_manager.read_diary(d_id)
            if diary:
                print("|> 일기를 성공적으로 불러왔습니다.")
                print(f'ID: {diary["diary_id"]} | 제목: {diary["diary_title"]}')
                print(f'게시일: {diary["diary_date"]}')
                print(f'날씨: {diary["diary_weather"]}')
                print(f'내용: {diary["diary_content"]}')
            else:
                print("|> 일기를 불러오지 못했습니다.")
        elif cmd == 3:
            d_id = int(input("|> 수정할 일기 ID를 입력하세요: "))
            content = input("|> 일기 내용을 입력하세요: ")
            if diary_manager.update_diary(d_id, content):
                print("|> 수정에 성공했습니다.")
            else:
                print("|> 수정에 실패했습니다.")
        elif cmd == 4:
            d_id = int(input("|> 삭제할 일기 ID를 입력하세요: "))
            if diary_manager.delete_diary(d_id):
                print("|> 삭제에 성공했습니다.")
            else:
                print("|> 삭제에 실패했습니다.")
        elif cmd == 5:
            d_id = int(input("|> 이어쓸 일기 ID를 입력하세요: "))
            content = input("|> 이어쓸 내용을 입력하세요: ")
            if diary_manager.append_to_diary(d_id, content):
                print("|> 이어쓰기에 성공했습니다.")
            else:
                print("|> 이어쓰기에 실패했습니다.")
        elif cmd == 6:
            break
        print()