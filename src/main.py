from fastapi import (
    Depends,
    FastAPI, 
    HTTPException,
    Request,
    )
from fastapi_limiter.depends import RateLimiter
import helpers
from pydantic import BaseModel
from decouple import config


REDIS_URL = config('REDIS_URL')
app = FastAPI()


@app.get("/")
def read_index():
    # helpers.generate-image()
    return {"hello":"world"}


class ImageGenerationRequest(BaseModel):
    prompt:str
    
@app.post('/generate')
def create_image(data: ImageGenerationRequest):
    try:
        pred_result = helpers.generate_image(data.prompt)
        return pred_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))