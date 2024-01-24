# Library-Management-System-API

This repository contains the code for a simple Library-Management-System-API with functionalities for user authentication, genre and book management, and data export.

## Getting Started

To run the API locally, follow the steps below:

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/thevanshs/Library-Management-System-API.git
    cd book-management-api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

The API will be accessible at `http://localhost:8000`.

## API Endpoints

### Common Endpoints

#### User Registration

- **Endpoint**: `/signup/`
- **Method**: POST
- **Example**:

    ```bash
    curl -X POST http://localhost:8000/signup/ -d "username=your_username&password=your_password"
    ```

#### User Login

- **Endpoint**: `/login/`
- **Method**: POST
- **Example**:

    ```bash
    curl -X POST http://localhost:8000/login/ -d "username=your_username&password=your_password"
    ```

### Admin Endpoints

#### Add Genre

- **Endpoint**: `/add_genre/`
- **Method**: POST
- **Example**:

    ```bash
    curl -X POST http://localhost:8000/add_genre/ -d "name=Fiction" -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

#### Get All Authors

- **Endpoint**: `/get_all_authors/`
- **Method**: GET
- **Example**:

    ```bash
    curl http://localhost:8000/get_all_authors/ -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
    ```

#### Export Books by Genre

- **Endpoint**: `/admin/export-books/<genre_id>/`
- **Method**: GET
- **Example** (JSON):

    ```bash
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:8000/admin/export-books/your_genre_id/
    ```

- **Example** (CSV):

    ```bash
    curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" http://localhost:8000/admin/export-books/your_genre_id/ > books_export.csv
    ```

### Author Endpoints

#### Add Book

- **Endpoint**: `/add-book/`
- **Method**: POST
- **Example**:

    ```bash
    curl -X POST http://localhost:8000/add-book/ -H "Authorization: Bearer YOUR_ACCESS_TOKEN" -d "name=BookName&genre=1&num_pages=100"
    ```

## Additional Notes

- Replace placeholders such as `YOUR_ACCESS_TOKEN` and `your_genre_id` with the actual values.
- Ensure you have the necessary permissions for admin and author-specific actions.
- For more details on each endpoint, refer to the code documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
