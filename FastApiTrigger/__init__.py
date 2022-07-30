import json

import azure.functions as func
import nest_asyncio
from fastapiapp.main import app

# This is important, or else your application may fail
nest_asyncio.apply()

# Congiguration: https://iotespresso.com/azure-function-to-fastapi-app-service/
async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req, context)