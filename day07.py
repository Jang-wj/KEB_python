# __init__ class 호출할 때 단 한번만 실행
# 상속으로 코드의 중복 해결할 수 있음

class Car:
    def exclaim(self):
        print("I'm a Car!")  # method


class Yugo(Car):
    def exclaim(self):  # method overriding 부모 클래스의 메서드를 대체
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")

    def need_push(self):  # method 추가
        print('A little help here?')

    pass


give_car = Car()
give_yugo = Yugo()
give_car.exclaim()
give_yugo.exclaim()
give_yugo.need_push()


class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):  # __init__ override
        self.name = 'Doctor' + name


class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ', Esquire'


person = Person('Kim')
doctor = MDPerson('Kim')
lawyer = JDPerson('Kim')
print(person.name, doctor.name, lawyer.name)


class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성 :", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능 스킬")
        # for i in (len(self.skills)):
        #     print(f'{i+1} : {self.skills[i]}')

    def attak(self, idx):
        print(f'{self.skills[idx]}공격 시전')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):  # super 부모클래스 호출
        super().__init__(owner, skills)
        self.name = '피카츄'
        print(f"피카츄")

    def attak(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]}공격 시전')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = '꼬부기'
        print(f'꼬부기')

    def attak(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]}공격 시전')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = '파이리'
        print(f'파이리')

    def attak(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]}공격 시전')


while True:
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 :')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄 2) 꼬부기 3) 파이리 :')
        if pokemon == '1':
            n = input('플레이어 이름 입렵 :')
            s = input('사용 가능한 기술 입력 :')
            p = Pikachu(n, s)
        elif pokemon == '2':
            n = input('플레이어 이름 입렵 :')
            s = input('사용 가능한 기술 입력 :')
            p = Ggoboogi(n, s)
        elif pokemon == '3':
            n = input('플레이어 이름 입렵 :')
            s = input('사용 가능한 기술 입력 :')
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라 주세요')
        p.info()
        skill = input('공격 번호 선택')
        p.attak(int(skill)-1)
    else:
        print('메뉴에서 골라 주세요')


# pi1 = Pikachu('한지우', '번개/100만 볼트')
# # pi1.info()
# ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기')
# # ggo1.info()
# ggo1.attak(2)
# ggo1.swim()
# # pi1.info()

# p1 = Pokemon('한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
