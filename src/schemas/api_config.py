from pydantic import BaseModel, Field, HttpUrl
from typing import Optional


class APIConfigBase(BaseModel):
    name: str = Field(..., description="API名称")
    base_url: HttpUrl = Field(..., description="API基础URL")
    api_key: Optional[str] = Field(None, description="API密钥")
    description: Optional[str] = None


class APIConfigCreate(APIConfigBase):
    pass


class APIConfigUpdate(BaseModel):
    name: Optional[str] = None
    base_url: Optional[HttpUrl] = None
    api_key: Optional[str] = None
    description: Optional[str] = None


class APIConfigInDB(APIConfigBase):
    id: int

    class Config:
        from_attributes = True


class APIConfig(APIConfigInDB):
    pass