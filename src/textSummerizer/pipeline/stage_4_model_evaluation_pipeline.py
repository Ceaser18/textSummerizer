from src.textSummerizer.config.configuration import ConfigurationManager

from src.textSummerizer.components.model_evaluation import ModelEvaluation

from src.textSummerizer.logging import logger

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass 

    def initiate_model_evaluation(self):
        logger.info("Initiating model evaluation")
        config_manager=ConfigurationManager()
        model_evaluation_config=config_manager.get_model_evaluation_config()

        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()

        logger.info("Model evaluation is completed")



