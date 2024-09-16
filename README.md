# Django Delights

Django Delights is a web application designed to manage a restaurant's menu, ingredients, recipes, and purchases. This project leverages the Django framework to provide a robust and scalable solution for restaurant management.

## Features

### Dashboard
- **List Today's Purchases**: View a list of all recorded purchases from the past 24 hours.
- **List Ingredients**: View a list of all ingredients with low inventory.
- **List Menu Items**: View a list of all menu items.

### Menu Management
- **Add Menu Items**: Create new menu items with details such as name, price, and image.
- **List Menu Items**: View a list of all menu items, sorted by name, with their recipe requirements.

### Ingredient Management
- **Add Ingredients**: Create new ingredients with name, quantity, unit, and unit price.
- **List Ingredients**: View a list of all ingredients and their quantities.

### Recipe Management
- **Add Recipe Requirements**: Define the ingredients and quantities required for each menu item.

### Purchase Management
- **Record Purchases**: Log purchases made by the restaurant, including details such as the item purchased. The user who logged the purchase and the date of purchase is included automatically.
- **List Purchases**: View a list of all recorded purchases.

### Profit and Revenue
- **View Revenue and Costs**: View a short summary of total revenue, cost and profit.

### Key Files and Directories

- **`djangodelights/`**: Contains the main Django project settings and configurations.
  - **`settings.py`**: Configuration for the Django project.
  - **`urls.py`**: URL routing for the project.

- **`inventory/`**: Contains the app-specific files for managing menu items, ingredients, recipes, and purchases.
  - **`templates/`**: Contains the templates for each webpage.
  - **`models.py`**: Defines the database models for Ingredient, MenuItem, RecipeRequirement, and Purchase.
  - **`views.py`**: Contains the views for handling HTTP requests related to menu items, ingredients, recipes, and purchases.
  - **`forms.py`**: Contains the form generics for the Ingredient, MenuItem, RecipeRequirement, and Purchase models.
  - **`admin.py`**: Configuration for the Django admin interface.
  - **`urls.py`**: URL routing for the inventory app.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/django_delights.git
    cd django_delights
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```sh
    python manage.py migrate
    ```

4. Run the development server:
    ```sh
    python manage.py runserver
    ```

5. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Adding Ingredients

1. Navigate to the "Ingredients" page and click the "Add New Ingredient" button.
2. Fill in the details for the new ingredient.
3. Click "Add Ingredient" to add the ingredient.

### Adding Menu Items

1. Navigate to the "Menu" page and click the "Add New Menu Item" button.
2. Fill in the details for the new menu item.
3. Click "Add Menu Item" to add the item to the menu.

### Adding Recipe Requirements

1. Navigate to the "Menu" page and click the "Add Recipe Requirement" button next to the desired menu item.
2. Fill in the ingredient details.
3. Click "Add Recipe Requirement" to add the recipe requirement.

### Recording Purchases

1. Navigate to the "Purchases" page and click the "Log New Purchase" button.
2. Fill in the purchase details.
3. Click "Record Purchase" to log the purchase.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Bootstrap for front-end styling](https://getbootstrap.com/)
- This project is based on Codecademy's Django Capstone Project in their [Build Python Web Apps with Django](https://www.codecademy.com/learn/paths/build-python-web-apps-with-django) course

---