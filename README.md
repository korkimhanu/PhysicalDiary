참조내용
=============

>### 가. 중요 내용 및 필참 내용
> git 관련한 내용입니다. cmd 창에서 이용하시면 됩니다. mac 사용자는 단톡방에서 대화 나눈 것과 같이 SSH키를 발급받고 이용해주시고, git hub에서 시작시에는 받고 종료후에는 업로드 해주세요
> 
>```commandline
>git pull origin master ::깃헙에서 업데이트 된 내용 받아오기
>git add . ::수정 완료 후 파일 추가
>git commit -m "수정한 버전 이름" ::개인 깃 리포지터리에 커밋
>git push origin master ::깃헙에 업로드
>```
>UI 수정방법
> >1. ![pycharm 프로젝트 파일 접속](/Images/UIprocess1.png)
> >
> >2. [여기](/venv/Scripts)로 이동
> >3. pySide6-designer.exe 실행
> >4. ![UI 열기](/Images/UIprocess2.png)
> >5. ![UI 열기2](/Images/UIprocess3.png)
> >6. 수정 후 ctr+s (UI만 수정했을 때도 File이 바뀐 것이므로 git add .부터 git push까지 해줘야함)
> >7. ctr+s만 하면 수정이 파이썬 코드에서는 수정이 안됨. 따라서 파이썬 코드 수정 필요
> >8. ![UI 저장](/Images/UIprocess4.png)
> >9. ![UI 저장](/Images/UIprocess5.png)
> >10. ![UI 저장](/Images/UIprocess6.png)
> 
>
>### 나. 코드 위치
> + [main code](main.py)
> + [UIs](UI)
>   + [MainScreen(Loby)](UI/ui_Loby.py)
> + [UI editor](venv/Scripts/pyside6-designer.exe) (UI를 코딩이 아닌 UI가 있는 에디터로 편집하고 싶을 떄 사용)
> 
>### 다. pyside6 & PyQt5 & git 관련 강의 모음
>1. [전반적인 강의](https://answer-me.tistory.com/category/pyside6)
>2. [시리얼모니터만들기](https://sc.sogang.ac.kr/bbs/bbsview.do?pkid=69555&bbsid=3857&wslID=mecha&searchField=&searchValue=&currentPage=1)
>3. [유튜브강의(pyQt5)](https://youtube.com/playlist?list=PL1eLKSeW1Baj72go6l3gg4C8TXRNUBdMo&si=sX0lmVDnQGDhhgUW)
>4. [유튜브강의(pyslide2)](https://www.youtube.com/playlist?list=PL1eLKSeW1Bah_G3DnTwQiytpMlET04LN7)
>5. [유튜브강의(pyslide6)](https://youtube.com/playlist?list=PLl0_N0yeFLesyK9nHoww-vL5As3aPlWgq&si=lxE_QT6QE4fkCmZd)
>6. [git에서 branch란?](https://git-scm.com/book/ko/v2/Git-%EB%B8%8C%EB%9E%9C%EC%B9%98-%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)
>7. [label 이미지 설정](https://martinii.fun/192)
>
> 
> [readme.md 수정방법](https://gist.github.com/ihoneymon/652be052a0727ad59601)