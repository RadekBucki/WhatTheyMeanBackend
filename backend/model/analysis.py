from bson import binary
from datetime import datetime
from typing import Optional

from mongodb_odm import Document

from backend.model.author_attitude import AuthorAttitude
from backend.model.file_type import FileType
from backend.model.status import Status


class Analysis(Document):
    name: str = "Analysis"
    start_date: datetime = datetime.now()
    finish_date: Optional[datetime] = None
    status: Status = Status.QUEUED
    file_type: Optional[FileType] = None
    link: Optional[str] = None
    raw_file: Optional[binary.Binary] = None
    full_transcription: Optional[str] = None
    video_summary: Optional[str] = None
    author_attitude: Optional[AuthorAttitude] = None
