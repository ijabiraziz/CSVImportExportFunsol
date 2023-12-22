from django.shortcuts import render, redirect
from django.http import HttpResponse
import pandas as pd
from .models import Author, Book, Genre
from django.core.files.storage import default_storage
from django.utils.datastructures import MultiValueDictKeyError


def export_csv(request):
    """
    Export a CSV file.

    Retrieves information about all books from the database and generates a CSV file
    containing columns for the title, author, and genres. The CSV file is then served as
    a downloadable attachment.

    * Headover to the 'http://127.0.0.1:8000/export/' URL endpoint. and click export button

    """

    if request.method == 'POST':
        books = Book.objects.all()
        data = {'Title': [], 'Author': [], 'Genres': []}

        for book in books:
            data['Title'].append(book.title)
            data['Author'].append(book.author.name)
            data['Genres'].append(', '.join(genre.name for genre in book.genres.all()))

        df = pd.DataFrame(data)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'
        df.to_csv(path_or_buf=response, index=False)
        return response
    print("Rendering export_csv.html")
    return render(request, 'csv_app/export_csv.html')


def import_csv(request):
    """
    this view reads the file,
    processes its content, and creates Author, Book, and Genre objects in the database accordingly.
    
    * Headover to the 'http://127.0.0.1:8000/import/' URL endpoint. and click "choose file" and import it.
    """
    if request.method == 'POST':
        try:
            file = request.FILES['file']
            df = pd.read_csv(file)

            #itterrows in pandas lets us easily loop through all the rows in csv file
            for index, row in df.iterrows():
                author_name = row['Author'] 
                author, created = Author.objects.get_or_create(name=author_name)

                book = Book.objects.create(
                    title=row['Title'],
                    author=author
                )

                genres_str = row['Genres']
                if pd.notna(genres_str):
                    genres_list = [genre.strip() for genre in genres_str.split(',')]
                    for genre_name in genres_list:
                        genre, created = Genre.objects.get_or_create(name=genre_name)
                        book.genres.add(genre)

            return redirect('import_csv')

        except MultiValueDictKeyError as e:
            print(f"Error: {e}")

    return render(request, 'csv_app/import_csv.html', {'books': Book.objects.all()})