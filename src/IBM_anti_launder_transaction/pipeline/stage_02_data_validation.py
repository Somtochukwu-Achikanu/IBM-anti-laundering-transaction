
from IBM_anti_launder_transaction.config.configuration import ConfigurationManager
from IBM_anti_launder_transaction.components.data_validation import DataValiadtion
from IBM_anti_launder_transaction import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f"Stage {STAGE_NAME} Started")
        obj = DataValidationTrainPipeline()
        obj.main()
        logger.info(f"Stage {STAGE_NAME} Completed")
    except Exception as e:
        logger.exception(e)
        raise e