import asyncio
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from sqlalchemy import select
from app.routers import auth, refunded, users, products, shipment, profile, marketplace, utils, orders, dashboard, supplier, inventory, AWB_generation, notifications
from app.database import Base, engine
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.emag_products import *
from app.utils.emag_orders import *
from app.utils.emag_refund import *
from app.utils.emag_reviews import *
from app.routers.reviews import *
from app.models.marketplace import Marketplace
from sqlalchemy.orm import Session
import logging



# member
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
# from module import Member, get_member, check_access

app = FastAPI()

class MemberResponse(BaseModel):
    username: str
    role_name: str
    access_level: str

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_models()

@app.on_event("startup")
@repeat_every(seconds=86400)  # Run daily for deleting video last 30 days
async def refresh_data(db: AsyncSession = Depends(get_db)):
    async for db in get_db():
        async with db as session:
            logging.info("Starting product refresh")
            result = await session.execute(select(Marketplace))
            marketplaces = result.scalars().all()
            logging.info(f"Success getting {len(marketplaces)} marketplaces")
            for marketplace in marketplaces:
                logging.info("Refresh product from marketplace")
                await refresh_products(marketplace, session)
                logging.info("Refresh refunds from marketplace")
                await refresh_refunds(marketplace)
                logging.info("Refresh order from marketplace")
                await refresh_orders(marketplace, session)
                logging.info("Check hijacker and review")
                await check_hijacker_and_bad_reviews(marketplace, session)
                

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])
app.include_router(marketplace.router, prefix="/api/marketplace", tags=["marketplace"])
app.include_router(utils.router, prefix="/api/utils", tags=["utils"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(supplier.router, prefix="/api/suppliers", tags=["supppliers"])
app.include_router(shipment.router, prefix="/api/shipment", tags=["shipment"])
app.include_router(refunded.router, prefix="/api/refunded", tags=["refunded"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["inventory"])
app.include_router(AWB_generation.router, prefix="/awb", tags=["awb"])
app.include_router(notifications.router, prefix='/api/notifications', tags=["notifications"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
