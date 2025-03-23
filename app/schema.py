from pydantic import BaseModel, HttpUrl


class BaseUrl(BaseModel):
    url: HttpUrl

class ShortUrlResponse(BaseModel):
    short_url: str
