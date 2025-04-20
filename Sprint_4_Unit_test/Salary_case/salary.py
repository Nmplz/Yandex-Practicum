class SalaryService:

    @staticmethod
    def calculate_salary(sales):
        percent = 5
        salary = sales * percent / 100
        salary_limit = 50000
        if salary > salary_limit:
            salary = salary_limit
        return salary
