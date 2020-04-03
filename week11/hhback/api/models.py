from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    city = models.CharField(max_length=30)
    address = models.TextField(default='')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    salary = models.FloatField(max_length=30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company_id': self.company_id
        }
