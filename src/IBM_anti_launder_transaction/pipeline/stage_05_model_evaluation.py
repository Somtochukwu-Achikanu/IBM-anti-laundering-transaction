
from IBM_anti_launder_transaction.config.configuration import ConfigurationManager
from IBM_anti_launder_transaction.components.model_evaluation import ModelEvaluation
from IBM_anti_launder_transaction import logger


STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        model_evaluation_config.save_results()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e