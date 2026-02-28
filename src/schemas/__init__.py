from .knowledge import (
    KnowledgeBase, KnowledgeCreate, KnowledgeUpdate,
    KnowledgeInDB, Knowledge, ContentType, FileUploadResponse
)
from .api_config import (
    APIConfigBase, APIConfigCreate, APIConfigUpdate,
    APIConfigInDB, APIConfig
)



# 数据验证：Pydantic 模型会自动校验前端传入的数据类型、长度、格式（比如邮箱是否合法），避免脏数据进入后端；
# 接口文档自动生成：FastAPI 会根据这些模型自动生成 Swagger/ReDoc 接口文档，前端能清晰看到需要传什么、返回什么；
# 代码解耦：把数据结构和业务逻辑（src/api）、数据库模型（src/models）分开，代码更清晰、易维护；
# 前后端约定：schemas 定义的结构就是前后端数据交互的 “契约”，避免双方理解不一致。
