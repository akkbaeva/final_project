from django.test import TestCase


# Create your tests here.
from category_food.models import Company, Dish


class TestCompanyModel(TestCase):

    def test_create_success(self):
        company_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'description': 'TestDescription'
        }
        company = Company.objects.create(**company_info)
        self.assertEqual(company.name, company_info['name'])
        self.assertEqual(company.image, company_info['image'])
        self.assertEqual(company.description, company_info['description'])

    def test_create_fail(self):
        company_info = {
            'name': 1,
            'image': '7.jpg',
            'description': 'TestDescription'
        }
        with self.assertRaises(ValueError):
            company = Company.objects.create(**company_info)

    def test_update(self):
        company_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'description': 'TestDescription'
        }
        new_name = 'Pati'
        company = Company.objects.create(**company_info)
        company.name = new_name
        company.save()
        company.refresh_from_db()
        self.assertEqual(company.name, new_name)
        self.assertEqual(company.image, company_info['image'])
        self.assertEqual(company.description, company_info['description'])

    def test_delete(self):
        company_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'description': 'TestDescription'
        }
        company = Company.objects.create(**company_info)
        pk = company.pk
        company.delete()
        company.refresh_from_db()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(pk=pk)


class TestDishModel(TestCase):
    def test_create_success(self):
        dish_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'company': 'TestCompany',
            'category': 'VEGETARIAN',
            'component': 'TestComponent'
        }
        dish = Dish.objects.create(**dish_info)
        self.assertEqual(dish.name, dish_info['name'])
        self.assertEqual(dish.image, dish_info['image'])
        self.assertEqual(dish.company, dish_info['company'])
        self.assertEqual(dish.category, dish_info['category'])
        self.assertEqual(dish.component, dish_info['component'])

    def test_create_fail(self):
        dish_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'company': 'TestCompany',
            'category': 1,
            'component': 'TestComponent'
        }
        with self.assertRaises(ValueError):
            dish = Dish.objects.create(**dish_info)

    def test_update(self):
        dish_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'company': 'TestCompany',
            'category': 'VEGETARIAN',
            'component': 'TestComponent'
        }
        new_name = 'Pika'
        dish = Dish.objects.create(**dish_info)
        dish.name = new_name
        dish.save()
        dish.refresh_from_db()
        self.assertEqual(dish.name, new_name)
        self.assertEqual(dish.image, dish_info['image'])
        self.assertEqual(dish.company, dish_info['company'])
        self.assertEqual(dish.category, dish_info['category'])
        self.assertEqual(dish.component, dish_info['component'])

    def test_delete(self):
        dish_info = {
            'name': 'TestName',
            'image': '7.jpg',
            'company': 'TestCompany',
            'category': 'VEGETARIAN',
            'component': 'TestComponent'
        }
        dish = Dish.objects.create(**dish_info)
        pk = dish.pk
        dish.delete()
        dish.refresh_from_db()
        with self.assertRaises(Dish.DoesNotExist):
            Dish.objects.get(pk=pk)
