class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name


employee_1 = Employee("성태호", 7000)
employee_2 = Employee("성태호", 7000)

cashier = Cashier("김대위", 9000)

employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier)

for employee in employee_list:
    employee.raise_pay()

total_wage = 0

for employee in employee_list:
    total_wage += employee.wage

print(total_wage)