from datetime import datetime, date, time

def get_employees():
    electricians = 13
    worker = 15
    result = electricians + worker
    print('Количество привлекаемых сотрудников:', result, '\n'
          'Текущая дата:', datetime.today())
if __name__ == '__main__':
    get_employees()
