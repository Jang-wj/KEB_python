# groups = {
#     '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
#     '마마무': ['문별', '솔라', '휘인', '화사']
# }
# for group, members in groups.items():
#     print(f'{group}의 멤버')
#     for member in members:
#         if member != '승리':
#             print(member)

# class

class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성 시 동작
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f'포켓몬 {name} 객체 생성됨')

    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill)

# p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
# # print(p1.name, p2.name)
# # print(f'{p1.owner}의 포켓몬은 {p1.name}입니다.')
# # print(f'{p2.owner}의 포켓몬은 {p2.name}입니다.')
# p1.info()
# p2.info()
# # print(p2.skills)


# inheritance
class Pikachu(Pokemon):
    pass


pi1 = Pikachu('피카츄', '인하', '번개')
pi1.info()
