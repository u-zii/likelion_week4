## 1번문제 ##
num=int(input("money를 입력하세요 : "))

def what(x):
    if x>=10000:
        print("고기를 먹는다")
    elif x>=5000:
        print("국밥을 먹는다")
    else:
        print("라면을 먹는다")

what(num)

## 2번문제 ##
fruits=[]

fruits.append(input("1번 과일을 입력하세요"))
fruits.append(input("2번 과일을 입력하세요"))
fruits.append(input("3번 과일을 입력하세요"))
fruits.append(input("4번 과일을 입력하세요"))
fruits.append(input("5번 과일을 입력하세요"))

for i in range(0,5):
    print(i+1, "번째 과일은", fruits[i], "입니다.")

## 3번문제 ##
cookies={'탱커':'우유맛쿠키','딜러':'칠리맛쿠키','힐러':'천사맛쿠키','서포터':'석류맛쿠키'}

for key,value in cookies.items():
    if key=='탱커':
        cookies['탱커']='다크초코맛쿠키'
    elif key=='딜러':
        cookies['딜러']='라떼맛쿠키'
    elif key=='힐러':
        cookies['힐러']='허브맛쿠키'

print(cookies)

# 4번문제 ##
def add():
    x=int(input("숫자 1을 입력하세요"))
    y=int(input("숫자 2를 입력하세요"))
    print(x+y)

def sub():
    x=int(input("숫자 1을 입력하세요"))
    y=int(input("숫자 2를 입력하세요"))
    print(x-y)

def mul():
    x=int(input("숫자 1을 입력하세요"))
    y=int(input("숫자 2를 입력하세요"))
    print(x*y)

def div():
    x=int(input("숫자 1을 입력하세요"))
    y=int(input("숫자 2를 입력하세요"))
    print(x/y)

while True:
    number=int(input("원하는 숫자를 입력하세요 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 종료"))

    if number==1:
        add()
    elif number==2:
        sub()
    elif number==3:
        mul()
    elif number==4:
        div()
    elif number==5:
        break
    else:
        continue

# 5번문제 ##
class Person:
    def __init__(self,name):
        self.name=name

    def hello(self):
        print("안녕 내 이름은", self.name, "이야")
    
    def walk(self):
        print("나는 걷는 중")

class Worker(Person):
    def __init__(self, name, company):
        Person.__init__(self, name)
        self.company=company
        self.mental=50

    def hello(self):
        print("안녕 내 이름은", self.name,"이고, 내가 다니는 회사는", self.company)

    def work(self):
        if self.mental>=0:
            print("나는 일하는 중, 내 멘탈 지수 : ",self.mental)
            self.mental-=10
        else:
            print("더는 일 못해")

worker = Worker("빌게이츠", "삼성")
worker.hello()
worker.walk()
for i in range(7):
    worker.work()