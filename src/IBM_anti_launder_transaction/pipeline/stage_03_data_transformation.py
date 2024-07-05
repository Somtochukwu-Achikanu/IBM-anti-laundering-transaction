
from IBM_anti_launder_transaction.config.configuration import ConfigurationManager
from IBM_anti_launder_transaction.components.data_transformation import DataTransformation
from IBM_anti_launder_transaction import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.get_data_transformation()
        data_transformation.save_preprocessor()
        data_transformation.train_test_split()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = DataTransformationTrainPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e