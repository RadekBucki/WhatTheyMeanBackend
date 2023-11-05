from datetime import datetime


class Analysis:
    def __init__(self, uuid, start_date, file_type, raw_file, name='Analysis', end_date=None, status='IN_PROGRESS',
                 link=None, full_transcription=None, video_summary=None, author_attitude=None):
        self.uuid = uuid
        if name == "Analysis":
            name = name + " " + uuid
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S') if end_date else end_date
        self.status = status
        self.file_type = file_type
        self.link = link
        self.raw_file = raw_file
        self.full_transcription = full_transcription
        self.video_summary = video_summary
        self.author_attitude = author_attitude

    @classmethod
    def from_dict(cls, data):
        return cls(uuid=data["uuid"], name=data["name"], start_date=data["start_date"], end_date=data["end_date"],
                   status=data["status"], file_type=data["file_type"],
                   link=data["link"], raw_file=data["raw_file"], full_transcription=data["full_transcription"],
                   video_summary=data["video_summary"],
                   author_attitude=data["author_attitude"])

    def to_dict(self):
        dict = {
            "uuid": self.uuid,
            "name": self.name,
            "start_date": self.start_date.strftime('%Y-%m-%d %H:%M:%S'),
            "end_date": self.end_date.strftime('%Y-%m-%d %H:%M:%S') if self.end_date else self.end_date,
            "status": self.status,
            "file_type": self.file_type,
            "link": self.link,
            "raw_file": self.raw_file,
            "full_transcription": self.full_transcription,
            "video_summary": self.video_summary,
            "author_attitude": self.author_attitude
        }
        return dict
