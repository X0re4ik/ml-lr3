import click
from models.services.file import get_file_service
from models.services.s3 import get_s3_service
from models.use_cases.data_processing import get_data_processing_use_case
from models.use_cases.download_data_from_bucket import \
    get_download_data_from_bucket_use_caseI
from models.use_cases.load_data_in_bucket import \
    get_load_data_in_bucket_use_case
from models.utils.s3_client import get_boto3_client


@click.command()
@click.option("--input_path", help="Путь до исходного файла")
@click.option("--external_path", help="Путь до промежуточного фала")
@click.option("--output_path", prompt="", help="Путь до обработоного файла")
@click.option("--s3_bucket_name", help="Наименование бакета")
@click.option("--s3_access_key_id", help="Access Key ID")
@click.option("--s3_secret_access_key", help="Secret Key ID")
@click.option("--s3_endpoint_url", help="Endpoint URL")
def pipeline(
    input_path: str,
    output_path: str,
    external_path: str,
    s3_bucket_name: str,
    s3_access_key_id: str,
    s3_secret_access_key: str,
    s3_endpoint_url: str,
):
    """Выполнить pipeline обрабтки данных для файла"""

    client = get_boto3_client(s3_access_key_id, s3_secret_access_key, s3_endpoint_url)

    s3_service = get_s3_service(client)
    file_service = get_file_service()
    _input_path = file_service.to_path(input_path, validate=True)
    _external_path = file_service.to_path(external_path)
    _output_path = file_service.to_path(output_path)

    if not _input_path.exists():
        raise Exception("Файл не найден")

    # Загрузить данные в s3 хранилище
    get_load_data_in_bucket_use_case(s3_bucket_name, s3_service, _input_path).execute()

    # Выгрузить данные из s3 хранилища
    get_download_data_from_bucket_use_caseI(
        s3_bucket_name, s3_service, _input_path.name, str(_external_path)
    ).execute()

    # Выполнить обработку данных
    get_data_processing_use_case(external_path, _output_path).execute()


if __name__ == "__main__":
    pipeline()
