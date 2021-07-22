class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surname}')

    def get_total_income(self,):
        person_wage = self._income.get('wage')
        person_bonus = self._income.get('bonus')
        print(f'Оклад сотрудника - {person_wage}р. , премия сотрудника - {person_bonus}р. , полная зарплата сотрудника составляет {person_wage + person_bonus}р.')

n = Position('Vladimir', 'Lucchese', 'CEO', 100000, 50000)
n.get_full_name()
n.get_total_income()



