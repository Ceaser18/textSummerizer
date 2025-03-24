from src.textSummerizer.config.configuration import ConfigurationManager

from src.textSummerizer.components.data_ingestion import DataIngestion

from src.textSummerizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_data_ingestion(self):
        logger.info("Initiating data ingestion")
        config_manager=ConfigurationManager()
        data_ingestion_config=config_manager.get_data_ingestion_config()

        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.downlaod_file()
        data_ingestion.extract_zip_file()

        logger.info("Data ingestion is completed")

