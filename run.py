from app import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081, debug=True)

from app.db.Employee import Employee
from app.db.Company import Company

emp = Employee("Samora Machel", "samoraok@gmail.com")
emp.set_password("password123")
print(emp._verify_password("password123"))
comp = Company("Bizup", "bizup@gmail.com", "password123")
# print(emp.displayJson())
# print(emp._verify_password("password123"))
# emp.insert()
