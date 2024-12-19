from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date
import datetime 

class Base(DeclarativeBase):
    pass

# We create a model for the database
class StgJobs(Base):
    __tablename__='stg_jobs'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True,  server_default='uuid_generate_v4()')

    title: Mapped[str] = mapped_column(String(16777216))
    subtitle: Mapped[str] = mapped_column(String(16777216))
    location: Mapped[str] = mapped_column(String(16777216))
    date: Mapped[str] = mapped_column(Date())

    def __repr__(self) -> str:
        return f"StgJobs(id={self.id!r}, title={self.title!r}, subtitle={self.subtitle!r}, location={self.location!r}, date={self.date!r})"
