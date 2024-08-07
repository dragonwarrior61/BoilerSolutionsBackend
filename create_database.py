import asyncio
import asyncpg
from app.config import settings

async def create_database():
    conn = await asyncpg.connect(
        user=settings.DB_USERNAME,
        password=settings.DB_PASSWORD,
        database='postgres',  # Connect to the default database
        host=settings.DB_URL,
        port=settings.DB_PORT
    )
    await conn.execute(f"""
        CREATE DATABASE {settings.DB_NAME}
    """)
    await conn.close()

if __name__ == "__main__":
    asyncio.run(create_database())
