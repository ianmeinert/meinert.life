from fastapi import FastAPI
from starlette.responses import HTMLResponse
# import locale files
from models import models
from database.configuration import engine
# import router files
from core import blog, user, auth
# import CORS middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Meinert.life API",
    description="This is the API for meinert.life blog",
    version="1.0.0",)

origins = [
    "http://meinert.life",
    "https://meinert.life",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!Doctype html>
    <html>
        <body>
            <h1>SecureAPI</h1>
            <div class="btn-group">
                <a href="/docs"><button>SwaggerUI</button></a>
                <a href="/redoc"><button>Redoc</button></a>
            </div>
        </body>
    </html>
"""
