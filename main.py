import logging
from src.textSummerizer.logging import logger

from src.textSummerizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"


try:
    logger.info(f"Initiating {STAGE_NAME}")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise Exception(f"{STAGE_NAME} failed") from e
