from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>College Basketball Tracker</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <h2>College Basketball Tracker</h2>
            <p>A place to keep track of college basketball games I want to watch.</p>
        </body>
        </html>
    """)