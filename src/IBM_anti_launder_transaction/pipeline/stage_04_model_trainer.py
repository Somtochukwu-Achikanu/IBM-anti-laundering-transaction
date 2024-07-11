
from IBM_anti_launder_transaction.config.configuration import ConfigurationManager
from IBM_anti_launder_transaction.components.model_trainer import ModelTrainer
from IBM_anti_launder_transaction import logger


STAGE_NAME = "Model Trainer Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e