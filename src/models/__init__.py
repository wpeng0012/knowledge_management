from .user import User
from .task import Task

# 更新User模型，添加关系
from sqlalchemy.orm import relationship

# 这里我们通过重新赋值的方式添加关系
# 在实际开发中，通常直接在类中定义
User.tasks = relationship("Task", back_populates="user")
Task.user = relationship("User", back_populates="tasks")