from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class S3Service:
    _client: Any

    def check_connection(self) -> bool:
        try:
            self._client.list_buckets()
            return True
        except Exception:
            return False

    def load_file_in_bucket(self, bucket_name: str, file: Path) -> str:
        path_to_file = file.name
        self._client.upload_file(str(file), bucket_name, path_to_file)
        return path_to_file

    def create_bucket_if_not_exist(self, bucket_name: str) -> bool:
        try:
            self._client.create_bucket(Bucket=bucket_name)
            return True
        except self._client.exceptions.BucketAlreadyExists:
            return False
        except self._client.exceptions.BucketAlreadyOwnedByYou:
            return False

    def unload_file_from_bucket(
        self, bucket_name: str, file_name: str, output_dir: str
    ) -> None:
        self._client.download_file(bucket_name, file_name, output_dir)


def get_s3_service(client) -> S3Service:
    return S3Service(_client=client)
