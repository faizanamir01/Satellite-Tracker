# Satellite-Tracker

The Satellite Tracker is a Django web application that allows users to track satellites and view information about their orbits, including their object names, IDs, epochs, mean motions, and other relevant data.


## Features

- Fetches satellite data from multiple sources based on predefined satellite names.
- Displays satellite data in a table format on the homepage.
- Displays data for satellite launch countries in second table.


## Installation

1. Clone the repository to your local machine:

    ```
    git clone <https://github.com/faizanamir01/Satellite-Tracker.git>
    ```

2. Navigate to the project directory:

    ```
    cd project
    ```

3. Install 'requests' using pip:

    ```
    pip install requests
    ```

4. Run migrations to create the necessary database tables:

    ```
    python manage.py migrate
    ```

5. Start the Django development server:

    ```
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Upon accessing the application, you will see a table displaying satellite data fetched from various sources.
- Additionally, there is a second table showing dummy data for satellite launch countries.

## Configuration

- To modify the list of satellite names or add new sources for satellite data, update the `satellite_names` list and `satellite_urls` dictionary in the `views.py` file.
- Customize the appearance of the tables or add additional features by modifying the HTML templates (`home.html`).

## Dependencies

- Django: The web framework used to build the application.
- Requests: A Python library for making HTTP requests to fetch satellite data from external sources.

