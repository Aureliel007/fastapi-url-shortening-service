from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from fastapi import HTTPException
from models import Session, Urls


async def add_url(session: Session, item: Urls) -> Urls:
    try:
        session.add(item)
        await session.commit()
    except IntegrityError as err:
        if err.orig.pgcode == "23505":
            await session.rollback()
            orm_obj = await session.execute(
                select(Urls).where(Urls.url == item.url)
            )
            item = orm_obj.scalars().first()
            return item
        raise err
    return item

async def get_target_url(session: Session, short_url: str) -> Urls:
    result = await session.execute(
        select(Urls).where(Urls.short_url == short_url)
    )
    orm_obj = result.scalars().first()
    if orm_obj is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return orm_obj
