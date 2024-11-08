from dataclasses import dataclass

from models.services.s3 import S3Service


@dataclass
class DownloadDataFromBucketUseCase:
    """Загрузить файл с локальной машины в S3"""

    _bucket_name: str
    _s3_service: S3Service
    _filename: str
    _output_file: str

    def execute(self):
        if self._s3_service.check_connection():
            raise Exception("")

        self._s3_service.unload_file_from_bucket(
            self._bucket_name, self._filename, self._output_file
        )


def get_download_data_from_bucket_use_caseI(
    bucket_name: str, s3_service: S3Service, filename: str, output_file: str
):
    return DownloadDataFromBucketUseCase(
        _bucket_name=bucket_name,
        _s3_service=s3_service,
        _filename=filename,
        _output_file=output_file,
    )
