# Задание 3
# Возьмите задачу о банкомате из семинара 2. Разбейте её на 
# отдельные операции — функции. Дополнительно сохраняйте все 
# операции поступления и снятия средств в список.


from random import randint
 
class User:
    def __init__(self, balance):
        self.balance = balance
 
 
class Cash_machine:
    data = {}
    reserve = 1000
 
    def checking(self, pin):
        if pin in self.data:
            self.user = self.data[pin]
            print(' OK ')
            return True
        else:
            print(' Code error ')
            
    def info(self):
        print(f' баланс {self.user.balance}')
 
    def withdraw(self, money):
        if money > self.user.balance:
            print('У вас недостаточно средств')
        elif money > self.reserve:
            print('В банкомате недостаточно средств')
        else:
            self.user.balance -= money
            self.reserve -= money
            print(f'Выдано {money}')
 
    def supplement(self, money):
        self.user.balance -= money
        self.reserve -= money
        print(f'Баланс пополнен на {money} ')
        
        
cash = Cash_machine()
for _ in range(10):
    pin = randint(1000, 9999)
    cash.data[pin] = User(randint(0, 1000))
 
print('Вам попали карты 10 пользователей')
print('  Вот их коды', *cash.data)
while True:
    pin = int(input('Введите pin или 0 для завершения: '))
    if pin == 0:
        break
    if not cash.checking(pin):
        continue
    while True:
        print('Выбор операции. 1 - просмотр, 2 - снять, 3 - пополнить, 4 - сменить карту')
        n = input()
        if n == '1':
            cash.info()
        elif n == '2':
            cash.withdraw(int(input('>>: ')))
        elif n == '3':
            cash.supplement(int(input('>>: ')))
        elif n == '4':
            break