from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    intensity = Column(Float)
    likelihood = Column(Float)
    relevance = Column(Float)
    country = Column(String)
    city = Column(String)
    topics = Column(String)
    region = Column(String)
    source = Column(String)
    pest = Column(String)
    swot = Column(String)