from application import salary
from application.db import people


def function():
  while True:
    interface_command = input('Выберете одну из команд нажав следующие клавиши: s, p. Для выхода наберите: exit. Для вызова справки наберите: help. Введите команду: ')
    print()
    if interface_command == 's':
      salary.calculate_salary()
      print()
    elif interface_command == 'p':
      people.get_employees()
      print()
    elif interface_command == 'exit':
      break
    elif interface_command == 'help':
      print('s – команда, которая вызовет результат расчета заработной платы сотрудника, l – команда, которая выведет количество привлекаемых сотрудников.')
      print()
    else:
      print('Такой комманды не существует в интерфейсе данной программы, повторите ввод!')
      print()
function()