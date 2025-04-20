from salary import SalaryService

class TestSalaryService:
    def test_calculate_salary_when_under_limit(self):
        actual = SalaryService.calculate_salary(50000)
        expected = 2500
        assert actual == expected 