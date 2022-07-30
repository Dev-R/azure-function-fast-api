from pydantic import BaseModel, HttpUrl


class TwitterVideoDownloaderModel(BaseModel):
    url: HttpUrl

class TwitterVideoDownloaderResponse(BaseModel):
    result: object