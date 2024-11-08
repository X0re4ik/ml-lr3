from dataclasses import dataclass
from pathlib import Path

from models.services.s3 import S3Service


@dataclass
class LoadDataInBucketUseCase:
    """Загрузить файл с локальной машины в S3"""

    _bucket_name: str
    _s3_service: S3Service
    _file: Path

    def execute(self):
        if self._s3_service.check_connection():
            raise Exception("")

        self._s3_service.create_bucket_if_not_exist(self._bucket_name)
        self._s3_service.load_file_in_bucket(self._bucket_name, self._file)


def get_load_data_in_bucket_use_case(
    bucket_name: str, s3_service: S3Service, file: Path
):
    return LoadDataInBucketUseCase(
        _bucket_name=bucket_name,
        _s3_service=s3_service,
        _file=file,
    )
