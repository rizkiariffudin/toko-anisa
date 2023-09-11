from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_create_instance(self):
        # Create an instance of Item
        my_model = Item(name="Roti", amount=10, description="Roti bakar enak")

        # Verify that the attributes match what you set
        self.assertEqual(my_model.name, "Roti")
        self.assertEqual(my_model.amount, 10)
        self.assertEqual(my_model.description, "Roti bakar enak")

    def test_save_and_retrieve(self):
        # Create an instance of Item
        my_model = Item(name="Pisang", amount=15, description="Pisang coklat")

        # Save it to the database
        my_model.save()

        # Retrieve the object from the database
        retrieved_model = Item.objects.get(name="Pisang")

        # Verify that the retrieved object matches the saved object
        self.assertEqual(retrieved_model.name, "Pisang")
        self.assertEqual(retrieved_model.amount, 15)
        self.assertEqual(retrieved_model.description, "Pisang coklat")