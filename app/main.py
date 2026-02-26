from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
# from app.modules.users.routes import router as user_router
# from app.modules.auth.router import router as auth_router

# from app.modules.products.routes import router as product_router

app = FastAPI(
    title="FastAPI Production App",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS settings
origins = [
    "http://localhost:3000",   
    "http://127.0.0.1:3000",
    "https://yourdomain.com", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


# # Include app-based routers
# app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
# app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(product_router, prefix="/api/v1/products", tags=["Products"])
