from app import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081, debug=True)

from app.db.Employee import Employee

emp = Employee("Samora Machel", "samoraok@gmail.com", "password123")
print(emp._verify_password("password123"))
# emp.insert()
