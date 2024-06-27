from src.IBM_anti_launder_transaction import logger
from src.IBM_anti_launder_transaction.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} Started")
    obj = DataIngestionTrainPipeline()
    obj.main()
    logger.info(f"Stage {STAGE_NAME} Completed!")

except Exception as e:
    logger.exception(e)
    raise e
