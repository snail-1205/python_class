"""
여기선 클래스를 만들어볼거임
js에서 클래스 만들어봤지? 똑같음 클래스도 대부분의 언어에서 지원함 (go Rust는 안하긴함 ㅋ)
"""

class Champion(): #만약 여기 괄호안에다가 다른 클래스를 넣으면 그 클래스를 상속받을 수 있음. js에서 ㄷ
    #js에서 constructor 생각하면 됨 파이썬에선 __init__이라는 웃기게생긴 말을 사용함
    def __init__(self, name) -> None:
        self.name = name #this.name =name 생각하면 됨.

    #메소드 선언은 그냥 def로 하면됨
    #근데 첫 인자로 무조건 self를 넣어줘야함. 
    #여기서 self는 인스턴스 자신을 얘기하는거임.
    def say(self, str):
        print(str)

    # 이런식으로 자기 이름을 말하게하려면 첫 인자로 넣어줬던 self를 사용하면됨. js에서 this 썼던거랑 다르지.

    def sayMyName(self):
        print(self.name)
        

# 새로운 챔피언 인스턴스를 만드려면 이렇게 하면 됨 new 없어도 되는게 특징
pyke = Champion("pyke")

pyke.say("안녕 내이름은")
pyke.sayMyName()