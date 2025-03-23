from sqlalchemy import String
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import DSN


engine = create_async_engine(DSN)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class Urls(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    short_url: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    @property
    def dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "short_url": self.short_url,
        }
