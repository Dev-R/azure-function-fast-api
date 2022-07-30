import os
from decouple import config
from typing import Any, Dict, List, Optional, Union
import ast
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = config('BACKEND_CORS_ORIGINS', [])

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            # Return converted str representation of list to list
            return ast.literal_eval(v)
        raise ValueError(v)
    
    PROJECT_NAME: str = config('PROJECT_NAME', '')

    # class Config:
    #     case_sensitive = True


settings = Settings()
