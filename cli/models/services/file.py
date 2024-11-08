from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileService:
    def to_path(self, file: str, validate: bool = False) -> Path:
        path = Path(file)
        if validate and not path.exists():
            raise FileNotFoundError(f"Не найден файл: {path}")
        return path


def get_file_service():
    return FileService()
