from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException


from fastapiapp.services.models import (
    TwitterVideoDownloaderModel,
    TwitterVideoDownloaderResponse
) 

from fastapiapp.services.helpers import (
    TwitterVideoDownloader
)

router = APIRouter()


@router.post(
    '/download-tweet-video/',
    response_model=TwitterVideoDownloaderResponse,
    summary='Download Twitter status video'
)
def download_tweet_media(data: TwitterVideoDownloaderModel):
    """
        Generate a Tweet video downloader object by using 3rd party script with all the information:

        - **url**: a valid http / https URL for twitter status 
                   i.e: https://twitter.com/user/status/media_id

        Documentation about the external CLI can be found here https://github.com/ytdl-org/youtube-dl
    """
    tw_downloader = TwitterVideoDownloader()
    # Call script
    tw_data = tw_downloader.extract_tweet_status_info(tweet_url=data.url)
    
    # Return response
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'result': tw_data
        }
    )
