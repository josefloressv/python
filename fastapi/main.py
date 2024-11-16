from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=JSONResponse)
def get_list():
    return [1, 2, 3]

@app.get("/contact", response_class=HTMLResponse)
def contact():
    return """
    <html>
        <head>
            <title>Contact</title>
        </head>
        <body>
            <h1>Contact</h1>
            <p>Send us an email at
                <a href="mailto:hola@test.com">hola@test.com</a>
            </p>
        </body>
    </html>
    """
