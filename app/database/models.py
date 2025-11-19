from datetime import datetime, UTC
from typing import List, Optional

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    telegram_user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(255), index=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(255))
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    language_code: Mapped[Optional[str]] = mapped_column(String(10))
    is_bot: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now(UTC), 
        onupdate=datetime.now(UTC)
    )
    
    user_chats: Mapped[List["UserChat"]] = relationship(back_populates="user")


class Chat(Base):
    __tablename__ = "chats"
    
    chat_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    type: Mapped[str] = mapped_column(String(50))
    title: Mapped[Optional[str]] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now(UTC), 
        onupdate=datetime.now(UTC)
    )
    
    user_chats: Mapped[List["UserChat"]] = relationship(back_populates="chat")


class UserChat(Base):
    __tablename__ = "user_chats"
    
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.telegram_user_id"), primary_key=True
    )
    chat_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("chats.chat_id"), primary_key=True
    )
    first_seen_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.now(UTC)
    )
    last_seen_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(UTC), 
        onupdate=datetime.now(UTC)
    )
    
    user: Mapped["User"] = relationship(back_populates="user_chats")
    chat: Mapped["Chat"] = relationship(back_populates="user_chats")
