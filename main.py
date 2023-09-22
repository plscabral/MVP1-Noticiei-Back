from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.auth_controller import include_route as auth_controller
from controllers.user_controller import include_route as user_controller
from controllers.term_controller import include_route as term_controller

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

auth_controller(app)
user_controller(app)
term_controller(app)
