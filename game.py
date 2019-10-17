#!/usr/bin/env python
"""
Игра крестики нолики
"""

def isint(check_int):
    """
    Проверка на целое
    """
    try:
        int(check_int)
        return True
    except ValueError:
        return False

# Класс Game реализует игру крестики-нолики

class Game:
    """Consructor"""
    def __init__(self):
        self.step1 = list()
        self.step2 = list()
        self.dic = {1: 1,
                    2: 2,
                    3: 3,
                    4: 4,
                    5: 5,
                    6: 6,
                    7: 7,
                    8: 8,
                    9: 9}
        self.win = (
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (3, 5, 7)
        )
    def draw_table(self):
        """Нарисовать поле"""
        self.field = (f"\n-------------\n│ {self.dic[1]} │ {self.dic[2]} | {self.dic[3]} "+
                      f"│\n-------------\n│ {self.dic[4]} │ {self.dic[5]} │ {self.dic[6]}"+
                      f"│\n-------------\n│ {self.dic[7]} │ {self.dic[8]} │ {self.dic[9]}"+
                      f"│\n-------------\n")
        print(self.field)

    def select_field(self):
        """Выбрать клетку, в которую поставить крестик или нолик"""
        print("Select the field")
        num = input()
        if not isint(num):
            print("Field must be int from 1 to 9 and must be vacant")
            return self.select_field()
        num = int(num)
        if ((num < 1) or (num > 9) or (self.dic[num] == "x") or (self.dic[num] == "○")):
            print("Field must be int from 1 to 9 and must be vacant")
            return self.select_field()
        return num

    def call_first(self, num):
        """Выбор клетки первого игрока"""
        self.dic.update({num : "x"})
        self.step1.append(num)
        self.step1.sort()
        self.draw_table()

    def call_second(self, num):
        """Выбор клетки второго игрока"""
        self.dic.update({num : "○"})
        self.step2.append(num)
        self.step2.sort()
        self.draw_table()

    def end(self):
        """Проверка, не закончились ли клетки на поле"""
        for _, dic_value in self.dic.items():
            if isint(dic_value):
                return False
        return True

    def game_end(self):
        """Проверка, совпадает ли выбранные игроками клетки набору победителя"""
        for i in self.win:
            j = 0
            for k_counter in self.step1:
                if i.count(k_counter) == 1:
                    j = j + 1
            if j == 3:
                return 1
            m_counter = 0
            for p_counter in self.step2:
                if i.count(p_counter) == 1:
                    m_counter = m_counter + 1
            if m_counter == 3:
                return 2
        if self.end():
            return 0
        return -1

    def check_res(self):
        """Проверить кто победил"""
        if self.game_end() == 1:
            print("First win")
            return "First win"
        if self.game_end() == 2:
            print("Second win")
            return "Second win"
        if self.game_end() == 0:
            print("Draw")
            return "Draw"
        return "Game continues"

    def game(self):
        """Старт игры"""
        print("First!")
        num = self.select_field()
        self.call_first(num)
        print("Second!")
        num = self.select_field()
        self.call_second(num)
        while self.game_end() == -1:
            num = self.select_field()
            self.call_first(num)
            if self.check_res() != "Game continues":
                return self.check_res()
            num = self.select_field()
            self.call_second(num)
            if self.check_res() != "Game continues":
                return self.check_res()

if __name__ == '__main__':
    NEW_GAME = Game()
    NEW_GAME.draw_table()
    NEW_GAME.game()
