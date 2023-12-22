# Django CSV Import/Export Assesment

This Project allows you to import and export data from CSV files. 
The project includes models representing books, authors, and genres, and provides functionalities to upload a CSV file containing book data, process it, and display the results.

## Features

- **CSV Import**: Upload a CSV file containing book information, and the application will create corresponding Author, Book, and Genre objects in the database.

- **CSV Export**: Export the existing book data to a CSV file for easy backup or sharing.

## Setup

1. Clone the repository:
    git clone https://github.com/ijabiraziz/CSVImportExportFunsol.git

2. Install the required dependencies:
    pip install -r requirements.txt

3. Apply database migrations:
    python manage.py migrate

4. Run the development server:
    python manage.py runserver

5. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1. Navigate to the http://127.0.0.1:8000/import/ page to upload a CSV file.

2. Click the http://127.0.0.1:8000/export/ button to download the existing book data in CSV format.

## Admin Panel
TO access django by default admin panel,
1. Open terminal and " python manage.py createsuperuser" (Provide all the required information and then visit http://127.0.0.1:8000/admin/
)


Thank You,
Jabir Aziz
