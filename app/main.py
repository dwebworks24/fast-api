from fastapi import FastAPI
from app.modules.users.routes import router as user_router
from app.modules.auth.routes import router as auth_router
# from app.modules.products.routes import router as product_router

app = FastAPI(
    title="FastAPI Production App",
    version="1.0.0"
)

# Include app-based routers
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
# app.include_router(product_router, prefix="/api/v1/products", tags=["Products"])
