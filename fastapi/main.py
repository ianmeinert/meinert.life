import os
import uvicorn
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from helper import FileUtility
# import locale files
from models import models
from database.configuration import engine
# import router files
from core import blog, user, auth
# import CORS middleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

properties_file = "configs/api.properties"
properties_dict = FileUtility.load_properties(properties_file)
origins = []

app = FastAPI(
    title=properties_dict["api.title"],
    description=properties_dict["api.description"],
    version=properties_dict["api.version"],)

for api_prop in properties_dict["api.origins"].split(','):
    origins.append[api_prop]

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
            <h1>meinert.life API</h1>
            <div class="btn-group">
                <a href="/docs"><button>SwaggerUI</button></a>
                <a href="/redoc"><button>Redoc</button></a>
            </div>
        </body>
    </html>
"""

if __name__ == '__main__':
    # run the application container
    uvicorn.run(app=app, port=properties_dict["api.port"], host=properties_dict["api.host"])