from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Date

class Base(DeclarativeBase):
    pass

# We create a model for the database
class StgJobs(Base):
    __tablename__='stg_jobs'
    title: Mapped[str] = mapped_column(String(16777216))
    subtitle: Mapped[str] = mapped_column(String(16777216))
    location: Mapped[str] = mapped_column(String(16777216))
    date: Mapped[str] = mapped_column(Date())

    def __repr__(self) -> str:
        return f"StgJobs(title={self.title!r}, subtitle={self.subtitle!r}, location={self.location!r}, date={self.date!r})"
