from datetime import datetime, date, time

def calculate_salary():
    debit = 16300
    credit = 14650
    result = debit + credit
    print('Заработная плата электромонтера составляет:', result, '\n'
          'Текущая дата:', datetime.today())
if __name__ == '__main__':
    calculate_salary()