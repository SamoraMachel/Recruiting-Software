from os import getenv
from typing import List
from app import create_app

app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8081, debug=True)

from app.controllers.NotificationController import Notification
from app.db.Employee import Employee
from app.db.Company import Company


data : List = Employee.read()
companyData = Company.read()

message = {"title":"Working Code","body":"The code has worked"}

samoraNotif = Notification(Company.toClassObject(companyData[0]), Employee.toClassObject(data[0]), message)
samoraNotif.setup_email(getenv("SENDER_EMAIL"), getenv("EMAIL_PASSWORD"))
samoraNotif.register_email()
samoraNotif.register_notification()



samoraNotif.notify()

# samoraNotif.notifier = "Wezacare"
# samoraNotif.notify()

# agesa = Notification("Bizup", "Agesa Collings", "Hello New User")
# agesa.register_notification()

# agesa.notify()
