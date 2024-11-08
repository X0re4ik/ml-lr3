#!/bin/sh
[ ! -f .env ] || export $(grep -v '^#' .env | xargs)

poetry run python cli/pipeline.py \
    --input_path=$(pwd)/data/interim/${ML_FILENAME} \
    --external_path=$(pwd)/data/external/external_${ML_FILENAME} \
    --output_path=$(pwd)/data/processed/processed_${ML_FILENAME} \
    --s3_bucket_name=${S3_BUCKET_NAME} \
    --s3_access_key_id=${S3_ACCESS_KEY} \
    --s3_secret_access_key=${S3_SECRET_ACCESS_KEY} \
    --s3_endpoint_url=${S3_ENDPOINT_URL}