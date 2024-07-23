from lib2to3.main import diff_texts
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a list of books
books = [
    {
        'id': 1,
        'title': 'Python 101',
        'author': 'Panwit Tu.',
    },
    {
        'id': 2,
        'title': 'Python 201',
        'author': 'Panwit Tu.',
    },
    {
        'id': 3,
        'title': 'Python 301',
        'author': 'Panwit Tu.',
    }
]


samliams = [
    {
        'id': 1,
        'base': 2,
        'high': 5,
    },
    {
        'id': 2,
        'base': 9,
        'high': 8,
    },
    {
        'id': 3,
        'base': 6,
        'high': 4,
    }
]


#help check for check api
@app.get('/api/v1/')
def root():
    return {
        'version': '1.0.0'
    }

@app.get('/api/v1/books')
def get_books():
    return books

@app.get('/api/v1/books/{book_id}')
def get_book(book_id: int, response: Response):
    for book in books:
        if book['id'] == book_id:
            return book
    response.status_code = 404
    return {
        'message': 'Book not found'
    }

@app.post('/api/v1/books')
def create_book(book: dict, response: Response):
    books.append(book)
    response.status_code = 201
    return book

@app.put('/api/v1/books/{book_id}')
def update_book(book_id: int, book: dict, response: Response):
    for i, b in enumerate(books):
        if b['id'] == book_id:
            books[i] = book
            return book
    response.status_code = 404
    return {
        'message': 'Book not found'
    }


@app.delete('/api/v1/books/{book_id}')
def delete_book(book_id: int, book: dict, response: Response):
    for i, b in enumerate(books):
        if b['id'] == book_id:
            del books[i]
    response.status_code = 404
    return {
        'message': 'Book not found'
    }

@app.get('/api/v1/triangles/{triangle_id}')
def area_triangle(triangle_id: int, response: Response, ):
    for triangle in samliams:
        if triangle['id'] == triangle_id:
            return {
                'area' : triangle['base'] * triangle['high'] * 0.5
            }
    response.status_code = 404
    return { 
        'message' : 'triangle not found'
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
