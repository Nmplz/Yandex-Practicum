class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=2, email=None):

        self.name = name
        self.rest_days = rest_days
        self.hours = hours
        self.email = email

    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = name + "@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
