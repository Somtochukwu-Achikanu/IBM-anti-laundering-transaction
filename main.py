from src.IBM_anti_launder_transaction import logger
from src.IBM_anti_launder_transaction.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from src.IBM_anti_launder_transaction.pipeline.stage_02_data_validation import DataValidationTrainPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed!")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataValidationTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed")

except Exception as e:
    logger.exception(e)
    raise e