from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


# 内容类型枚举
class ContentType(str, Enum):
    TEXT = "text"  # 文本笔记
    LINK = "link"  # 网址链接
    FILE = "file"  # 上传的文件
    API_DATA = "api_data"  # 从API获取的数据


# 基础模式
class KnowledgeBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="标题")
    description: Optional[str] = Field(None, description="描述")
    content: str = Field(..., description="内容/文件路径/URL/API数据")
    content_type: ContentType = ContentType.TEXT
    tags: List[str] = Field(default_factory=list, description="标签")


# 创建请求
class KnowledgeCreate(KnowledgeBase):
    pass


# 更新请求
class KnowledgeUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None


# 数据库模型
class KnowledgeInDB(KnowledgeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# API响应
class Knowledge(KnowledgeInDB):
    pass


# 文件上传响应
class FileUploadResponse(BaseModel):
    filename: str
    file_path: str
    content_type: str
    size: int