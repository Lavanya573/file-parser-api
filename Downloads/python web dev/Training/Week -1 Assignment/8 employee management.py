class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):  # ✅ self added here
        print('\n--- Employee Information ---')
        print('Employee ID:', self.__emp_id)
        print('Name:', self.__name)
        print('Salary: ₹', self.__salary)

    def hike(self, percent):
        hike_amount = self.__salary * (percent / 100)
        self.__salary += hike_amount
        print(f"Salary increased by {percent}%. New salary: ₹{self.__salary:.2f}")
#  MAIN
# emp = Employee("E001", "Lavanya", 50000)
# emp.display_info()
# emp.hike(15)
# emp.display_info()
try:
    # 1. Take user input
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Current Salary (₹): "))

    # 2. Create Employee object
    emp = Employee(emp_id, name, salary)

    # 3. Show employee info
    emp.display_info()

    # 4. Ask for hike %
    percent = float(input("\nEnter Hike Percentage (%): "))
    emp.hike(percent)

    # 5. Show updated info
    emp.display_info()

except ValueError:
    print(" Error: Please enter valid numeric values for salary or hike percent.")
