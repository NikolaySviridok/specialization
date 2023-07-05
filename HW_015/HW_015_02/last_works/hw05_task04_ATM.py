# 4. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и
# снятия средств в список.
from decimal import Decimal
from decimal import InvalidOperation
import logging


class ATM:
    class Display:
        _GREETING = '''
         WELCOME! DIY ATM greets You.
         Sum multiplicity is 50.0 units.
         TAXES:
         1.5% of sum but not lesser than 30 and not greater than 600 units.
         3% of refinancing after 3 operations performed.
         10% after each operation if account amount is greater than 5e6 units.
         '''
        _menu: tuple

        def __init__(self, actions: tuple) -> None:
            self._menu = actions
            print(self._GREETING)

        def print_menu(self):
            print("\nMAIN MENU:")
            print('\n'.join([f'{i:10}{label:>30}' for i, label in enumerate(self._menu, start=1)]))
            print()

        @staticmethod
        def print_text(text) -> None:
            print(text)

        def choose(self) -> str:
            return self._menu[self.get_menu_punct()]

        def get_menu_punct(self) -> int:
            pointer = -1
            while True:
                try:
                    pointer = int(input("Input your choice: ")) - 1
                except (TypeError, ValueError):
                    print("Wrong input")
                if 0 <= pointer < len(self._menu):
                    return pointer
                else:
                    print("Wrong input")

        @staticmethod
        def get_amount() -> Decimal:
            money_amt = -1
            while True:
                try:
                    money_amt = Decimal(input("Input amount of money: "))
                except (TypeError, InvalidOperation):
                    print("Wrong input")
                else:
                    if not money_amt % 50:
                        print(f'You entered:{round(money_amt, 2):.30}')
                        return money_amt
                    else:
                        print('Amount is not multiple of 50.00 units')

    _ACTIONS: tuple = ('TAKE', 'PUT', 'CHECK', 'GET OPERATIONS HISTORY', 'EXIT')
    _account_sum: Decimal = 0
    TAX_STANDARD: Decimal = Decimal(0.015)
    REFINANCE_RATE: Decimal = Decimal(0.03)
    TAX_WEALTH: Decimal = Decimal(0.1)
    CEILING_SUM: Decimal = Decimal(5e6)
    TAX_UPPER_LIM: Decimal = Decimal(600)
    TAX_LOWER_LIM: Decimal = Decimal(600)
    DIVISOR: Decimal = Decimal(50)

    def __init__(self) -> None:
        FORMAT = '{asctime} - {levelname}: {msg}'
        logging.basicConfig(filename='ATM_working.log', format=FORMAT, style='{',
                            filemode='a', level=logging.NOTSET)
        self._logger = logging.getLogger(__name__)

        self._operation_count = 0
        self.display = self.Display(self._ACTIONS)
        self._operations_list: list = []
        self._logger.info(msg=f'ATM started, operations: {self._operation_count}')

    def get_money_rest(self) -> Decimal:
        return self._account_sum

    def get_operations_list(self) -> str:
        return '\n' + '\n'.join(
            [f'{item[0]:.<30} {(item[1]):<20.2f}'
             for item in self._operations_list
             ]) + '\n'

    def put(self) -> None:
        log_string = 'Action: putting money.'
        self.display.print_text('Input amount of money to put: ')
        sum_to_put = self.display.get_amount()
        self._account_sum += sum_to_put
        self._operation_count += 1
        self._operations_list.append(("Income:", Decimal(sum_to_put)))
        log_string += f' Income: {sum_to_put}; operations count: {self._operation_count}'
        if self._account_sum > self.CEILING_SUM:
            tax_sum = self._account_sum * self.TAX_WEALTH
            self._account_sum -= tax_sum
            self._operations_list.append(('WEALTH TAX: ', -tax_sum))
            log_string += f' WEALTH TAX: {-tax_sum}'
        if self._operation_count > 3:
            refinance = self._account_sum * self.REFINANCE_RATE
            self._account_sum += refinance
            self._operations_list.append(("Income:", refinance))
            log_string += f' Refinance income: {refinance}'
        self.check()
        self._logger.info(msg=log_string)

    def take(self) -> None:
        log_string = 'Action: taking money.'
        self.display.print_text('Input amount of money to take: ')
        sum_to_take = self.display.get_amount()
        if self.get_money_rest() < sum_to_take:
            self.display.print_text('Not enough money!')
            log_string += f' Not enough money.'
        else:
            self._account_sum -= sum_to_take
            self._operation_count += 1
            self._operations_list.append(("Outcome:", -sum_to_take))
            tax_standard = sum_to_take * self.TAX_STANDARD
            log_string += f' Outcome: {sum_to_take}; operations count: {self._operation_count}'
            if tax_standard > 600:
                tax_standard = 600
            elif tax_standard < 30:
                tax_standard = 30
            self._account_sum -= tax_standard
            self._operations_list.append(('TAX FOR TAKING: ', -tax_standard))
            log_string += f' TAX FOR TAKING: {-tax_standard}'
            if self._account_sum > self.CEILING_SUM:
                tax_sum = self._account_sum * self.TAX_WEALTH
                self._account_sum -= tax_sum
                self._operations_list.append(('WEALTH TAX: ', -tax_sum))
                log_string += f' WEALTH TAX: {-tax_sum}'
            if self._operation_count > 3:
                refinance = self._account_sum * self.REFINANCE_RATE
                self._account_sum += refinance
                self._operations_list.append(("Income:", refinance))
                self._operation_count = 0
                log_string += f' Refinance income: {refinance}; operations count: {self._operation_count}'
        self.check()
        self._logger.info(msg=log_string)

    def check(self) -> None:
        self.display.print_text('Rest money on account:')
        self.display.print_text(f'{self.get_money_rest():.2f}')

    def check_operation(self) -> None:
        if self._account_sum > self.CEILING_SUM:
            tax_sum = self._account_sum * self.TAX_WEALTH
            self._account_sum -= tax_sum
            self._operations_list.append(('WEALTH TAX: ', -tax_sum))
        self.check()

    def work(self) -> None:
        while True:
            self.display.print_menu()
            match self.display.choose():
                case 'TAKE':
                    self.take()
                case 'PUT':
                    self.put()
                case 'CHECK':
                    self.check()
                case 'GET OPERATIONS HISTORY':
                    self.display.print_text(self.get_operations_list())
                case 'EXIT':
                    self.display.print_text("Good-bye! Exiting...")
                    self._logger.info(msg="Exiting ATM.")
                    raise SystemExit(0)
                case _:
                    self.display.print_text("ERROR! Internal error")


if __name__ == '__main__':
    print("Not for separate use")