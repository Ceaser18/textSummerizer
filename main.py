import logging
from src.textSummerizer.logging import logger

from src.textSummerizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummerizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.textSummerizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
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


STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f"Initiating {STAGE_NAME}")
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} is completed")
except Exception as e:
    logger.error(f"{STAGE_NAME} failed")
    logger.error(str(e))
    raise Exception(f"{STAGE_NAME} failed") from e


STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e



