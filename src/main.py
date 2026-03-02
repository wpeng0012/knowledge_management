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

# knowledge_management/
# ├── .idea/                  # PyCharm 项目配置
# ├── .venv/                  # 项目虚拟环境
# ├── src/                    # 核心源代码
# │   ├── api/                # API 路由层
# │   │   └── v1/             # v1 版本接口
# │   │       └── __init__.py # 路由导出
# │   ├── core/               # 核心配置与数据库连接
# │   │   ├── __init__.py
# │   │   ├── config.py       # 全局配置（环境变量、密钥等）
# │   │   └── database.py     # SQLAlchemy 引擎与会话管理
# │   ├── crud/               # 数据库操作层
# │   │   ├── __init__.py
# │   │   └── knowledge.py    # 知识条目 CRUD 操作
# │   ├── models/             # 数据库 ORM 模型
# │   │   ├── __init__.pygit s
# │   │   ├── task.py         # 任务表模型
# │   │   └── user.py         # 用户表模型
# │   ├── schemas/            # Pydantic 数据验证模型
# │   │   ├── __init__.py
# │   │   ├── api_config.py   # API 通用配置（分页、响应格式）
# │   │   └── knowledge.py    # 知识条目请求/响应模型
# │   ├── services/           # 业务逻辑层
# │   │   └── __init__.py     # 业务逻辑封装（如用户登录、知识创建）
# │   ├── utils/              # 通用工具层
# │   │   └── __init__.py     # 工具函数（密码加密、JWT、时间处理等）
# │   ├── __init__.py
# │   └── main.py             # FastAPI 应用入口
# ├── tests/                  # 测试用例
# │   └── __init__.py
# ├── .env                    # 环境变量（数据库 URL、密钥等）
# ├── requirements.txt        # 项目依赖
# └── README.md               # 项目说明文档