from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str

    def greet(self):
        return f'Вас приветствует {self.name}. Моя почта {self.email}'
    
    def __str__(self):
        return self.greet()

def main():
    Pavel = User(1, 'Pavel', 'p@ya.ru')
    print(Pavel)

main()