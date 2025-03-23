import fastapi
from fastapi.responses import RedirectResponse

from lifespan import lifespan
from schema import BaseUrl, ShortUrlResponse
from dependencies import SessionDependency
from utils import hash_url
from models import Urls
from crud import add_url, get_target_url


app = fastapi.FastAPI(
    title="URL shortening API",
    description="Welcome to API service for URL shortening",
    version="0.1.0",
    lifespan=lifespan
)


@app.post("/", response_model=ShortUrlResponse, status_code=201)
async def shorten_url(url: BaseUrl, session: SessionDependency):
    url = str(url.url)
    short_url = await hash_url(url)
    item = Urls(url=url, short_url=short_url)
    item = await add_url(session, item)
    return {"short_url": item.short_url}


@app.get("/{short_url}")
async def get_url(short_url: str, session: SessionDependency):
    item = await get_target_url(session, short_url)
    target_url = item.url
    return RedirectResponse(
        url=target_url,
        status_code=fastapi.status.HTTP_307_TEMPORARY_REDIRECT
    )
