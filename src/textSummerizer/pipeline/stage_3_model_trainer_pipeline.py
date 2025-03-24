from src.textSummerizer.config.configuration import ConfigurationManager

from src.textSummerizer.components.model_trainer import ModelTrainer

from src.textSummerizer.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_model_training(self):
        logger.info("Initiating model training")
        config_manager=ConfigurationManager()
        model_training_config=config_manager.get_model_trainer_config()

        model_trainer=ModelTrainer(config=model_training_config)
        model_trainer.train_model()

        logger.info("Model training is completed")

