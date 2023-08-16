from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.honeys_fragrance.core.settings import settings


connection_uri = settings.db.DATABASE_URL
print("connection ===", connection_uri)
if connection_uri.startswith("postgres://"):
    connection_uri = connection_uri.replace("postgres://", "postgresql://", 1)


engine = create_engine(
    connection_uri,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
