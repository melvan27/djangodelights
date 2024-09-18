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
You can explore the project at the deployed AWS link: [http://3.132.126.215/](http://3.132.126.215/). Alternatively, you can run the project on your own computer following the installation instructions below.

### Prerequisites

- Python 3.8+
- Django 5.1

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/melvan27/djangodelights.git
    cd djangodelights
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

## API

The project also includes an API that can be used to interact with the system programmatically. The API endpoints allow for CRUD operations on menu items, ingredients, recipes, and purchases.

### Getting Started with the API

To get started with the API, you can use Postman to make requests. Follow these steps:

### 1. Obtain a JWT (JSON Web Token)

1. Open Postman and create a new POST request.
2. Set the URL to `http://3.132.126.215/api/token/`.
3. In the "Body" tab, select "x-www-form-urlencoded" and set the format to "JSON".
4. Enter your username and password in the following format:
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
5. Click "Send". If the credentials are correct, you will receive a response containing the access and refresh tokens:
    ```json
    {
        "access": "your_access_token",
        "refresh": "your_refresh_token"
    }
    ```
Your access token will last for 1 hour.

### 2. Using the JWT

For all subsequent API requests, you need to include the access token in the Authorization header.

1. In Postman, create a new request (GET, POST, PUT, DELETE).
2. In the "Headers" tab, add a new header:
    - Key: `Authorization`
    - Value: `Bearer your_access_token`

### 3. API Endpoints
For all endpoints, select "raw" and choose JSON format for the Body.

#### Menu Items

- **GET /api/menu-items/**: Retrieve a list of all menu items.
- **POST /api/menu-items/**: Create a new menu item.
    ```json
    {
        "name": "New Menu Item",
        "price": 10.99,
        "image_url": "image-link.com"
    }
    ```
- **GET /api/menu-items/{id}/**: Retrieve a specific menu item by ID.
- **PUT /api/menu-items/{id}/**: Update a specific menu item by ID.
    ```json
    {
        "name": "Updated Menu Item",
        "price": 12.99,
        "image_url": "image-link.com"
    }
    ```
- **DELETE /api/menu-items/{id}/**: Delete a specific menu item by ID.

#### Ingredients

- **GET /api/ingredients/**: Retrieve a list of all ingredients.
- **POST /api/ingredients/**: Create a new ingredient.
    ```json
    {
        "name": "New Ingredient",
        "quantity": 100,
        "unit": "grams",
        "unit_price": 1.50
    }
    ```
- **GET /api/ingredients/{id}/**: Retrieve a specific ingredient by ID.
- **PUT /api/ingredients/{id}/**: Update a specific ingredient by ID.
    ```json
    {
        "name": "Updated Ingredient",
        "quantity": 150,
        "unit": "grams",
        "unit_price": 1.75
    }
    ```
- **DELETE /api/ingredients/{id}/**: Delete a specific ingredient by ID.

#### Recipe Requirements

- **GET /api/recipe-requirements/**: Retrieve a list of all recipe requirements.
- **POST /api/recipe-requirements/**: Create a new recipe requirement.
    ```json
    {
        "menu_item": 1,
        "ingredient": 2,
        "quantity": 3
    }
    ```
- **GET /api/recipe-requirements/{id}/**: Retrieve a specific recipe requirement by ID.
- **PUT /api/recipe-requirements/{id}/**: Update a specific recipe requirement by ID.
    ```json
    {
        "menu_item": 1,
        "ingredient": 2,
        "quantity": 2
    }
    ```
- **DELETE /api/recipe-requirements/{id}/**: Delete a specific recipe requirement by ID.

#### Purchases

- **GET /api/purchases/**: Retrieve a list of all purchases.
- **POST /api/purchases/**: Create a new purchase.
    ```json
    {
        "menu_item": 1,
        "quantity": 2
    }
    ```
- **GET /api/purchases/{id}/**: Retrieve a specific purchase by ID.
- **PUT /api/purchases/{id}/**: Update a specific purchase by ID.
    ```json
    {
        "menu_item": 1,
        "quantity": 3
    }
    ```
- **DELETE /api/purchases/{id}/**: Delete a specific purchase by ID.

By following these steps, you can interact with the Django Delights API using Postman. Make sure to replace `your_access_token` with the actual token you received during the authentication step.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/5.1/)
- [Bootstrap for front-end styling](https://getbootstrap.com/)
- This project is based on Codecademy's Django Capstone Project in their [Build Python Web Apps with Django](https://www.codecademy.com/learn/paths/build-python-web-apps-with-django) course

---