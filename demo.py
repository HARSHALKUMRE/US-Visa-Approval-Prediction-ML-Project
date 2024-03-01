import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.pipeline.training_pipeline import TrainPipeline

try:
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
except Exception as e:
    raise USvisaException(e, sys) from e