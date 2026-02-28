from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import or_

from src.crud.base import CRUDBase
from src.models.knowledge import Knowledge
from src.schemas.knowledge import KnowledgeCreate, KnowledgeUpdate


class CRUDKnowledge(CRUDBase[Knowledge, KnowledgeCreate, KnowledgeUpdate]):
    def search(
            self,
            db: Session,
            *,
            keyword: Optional[str] = None,
            tag: Optional[str] = None,
            content_type: Optional[str] = None,
            skip: int = 0,
            limit: int = 100
    ) -> List[Knowledge]:
        """搜索知识项"""
        query = db.query(Knowledge)

        if keyword:
            # 在标题和描述中搜索关键词
            query = query.filter(
                or_(
                    Knowledge.title.contains(keyword),
                    Knowledge.description.contains(keyword)
                )
            )

        if tag:
            # 搜索标签（简化实现，实际可能需要JSON字段查询）
            query = query.filter(Knowledge.tags.contains(tag))

        if content_type:
            query = query.filter(Knowledge.content_type == content_type)

        # 按更新时间倒序
        query = query.order_by(Knowledge.updated_at.desc())

        return query.offset(skip).limit(limit).all()

    def get_by_tag(self, db: Session, *, tag: str) -> List[Knowledge]:
        """按标签获取知识项"""
        return db.query(Knowledge).filter(
            Knowledge.tags.contains(tag)
        ).order_by(Knowledge.updated_at.desc()).all()

    def get_all_tags(self, db: Session) -> List[str]:
        """获取所有不重复的标签"""
        all_items = db.query(Knowledge).all()
        tags = set()
        for item in all_items:
            tags.update(item.tags)
        return list(tags)


# 创建实例
knowledge = CRUDKnowledge(Knowledge)