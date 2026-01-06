from sqlalchemy import Column, Integer, String, Numeric, DateTime, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Bill(Base):
    __tablename__ = "bills"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    bill_name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)  # utilities, rent, insurance, etc.
    amount = Column(Numeric(10, 2), nullable=False)
    due_date = Column(Date, nullable=False)
    is_recurring = Column(Boolean, default=False)
    frequency = Column(String(20), nullable=True)  # monthly, weekly, yearly
    is_paid = Column(Boolean, default=False)
    paid_date = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    user = relationship("User", back_populates="bills")