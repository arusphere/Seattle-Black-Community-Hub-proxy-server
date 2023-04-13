The Seattle-Black-Community-Hub-proxy-server is a Python-based web application built using the Flask framework. It provides a RESTful API that allows users to perform CRUD (create, read, update, delete) operations on resources related to black-owned businesses and historical sites in the Seattle area.

The backend program consists of several components:

### **`app` package**

The **`app`** package contains the core application logic and configuration settings. It includes the following sub-packages and modules:

- **`models`**: Defines the data models for the resources managed by the API (e.g., restaurants, historical sites, etc.)
- **`routes.py`**: Defines the API routes and request handlers for each resource
- **`__init__.py`**: Initializes the Flask application and database connection

### **`config.py` module**

The **`config.py`** module contains configuration settings for the Flask application and other components, such as the database connection.

### **`manage.py` script**

The **`manage.py`** script provides command-line tools for managing the application, such as running the development server, creating database tables, and populating the database with test data.

### **`requirements.txt` file**

The **`requirements.txt`** file lists the Python packages required by the application, including Flask, SQLAlchemy, and other dependencies.

## **Running the Backend Program**

To run the backend program, follow these steps:

1. Clone the repository to your local machine
2. Install the required Python packages by running **`pip install -r requirements.txt`**
3. Create a new database by running **`python manage.py create_db`**
4. Populate the database with test data by running **`python manage.py seed_db`**
5. Start the development server by running **`python manage.py runserver`**

Once the server is running, you can access the API endpoints by sending HTTP requests to the appropriate URL paths. For example, to get a list of all restaurants in the database, send a GET request to **`/restaurants`**.
