from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.database import engine, Base
from .models import user, task  # 导入模型以创建表
from .core.config import settings

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建FastAPI应用实例
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #  # 允许所有域名访问（生产环境必须改成具体域名，比如["https://yourdomain.com"]）
    allow_credentials=True,# 允许前端携带cookie等凭证信息
    allow_methods=["*"],# 允许所有HTTP方法（GET/POST/PUT/DELETE等）
    allow_headers=["*"], # 允许所有请求头（比如自定义的Token头、Content-Type等）
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to TaskMaster API",
        "version": settings.VERSION,
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# 1. 创建FastAPI应用实例
# 2. 配置中间件
# 3. 包含路由（API端点）
# 4. 启动数据库连接
# 5. 配置异常处理
# 6. 启动应用服务器

# uvicorn src.main:app --reload

