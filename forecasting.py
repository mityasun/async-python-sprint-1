import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from tasks import (
    DataAnalyzingTask, DataCalculationTask,
    DataFetchingTask, DataAggregationTask
)
from utils import CITIES, logger


def forecast_weather() -> str:

    logger.debug('Running ThreadPoolExecutor() for make_request')
    with ThreadPoolExecutor(max_workers=10) as pool:
        forecasts = pool.map(DataFetchingTask().make_request, CITIES.keys())

    logger.debug('Running ProcessPoolExecutor() for %s cities models')
    cores_count = multiprocessing.cpu_count()
    with ProcessPoolExecutor(max_workers=cores_count - 1) as executor:
        data = executor.map(
            DataCalculationTask().general_calculation, forecasts
        )

    logger.debug('Add rating for cities')
    result_data = DataCalculationTask().adding_rating(data)

    logger.debug('Write results to json file')
    DataAggregationTask(threading.RLock()).save_results_to_json(result_data)

    logger.debug('Return the best city by weather conditions')
    return DataAnalyzingTask().get_result(result_data)


if __name__ == "__main__":
    print(forecast_weather())
