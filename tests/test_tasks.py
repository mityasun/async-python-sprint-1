from pathlib import Path

from models import (CityModel, FinalResultsModel, DayTempConditionModel,
                    CityWeatherDayModel, ListDaysModel, DatesModel, HoursModel,
                    RatingCityListModel, RatingCityModel)
from tasks import (DataAggregationTask, DataAnalyzingTask, DataCalculationTask,
                   DataFetchingTask)
from utils import RESULT_FILE, CITIES


def test_fetching_data_from_api(city='MOSCOW'):
    """Test for DataFetchingTask()"""

    city_data = DataFetchingTask().make_request(city_name=city)
    assert city_data.city == city
    assert type(city_data) == CityModel
    assert type(city_data.forecasts) == ListDaysModel
    assert type(city_data.forecasts.forecasts[0]) == DatesModel
    assert city_data.forecasts.forecasts[0].date == '2022-05-26'
    assert type(city_data.forecasts.forecasts[0].hours[0]) == HoursModel
    assert city_data.forecasts.forecasts[0].hours[0] == HoursModel(
        hour=0, temp=10, condition='overcast'
    )


def test_calculating_data(city_data: CityModel):
    """Test for calculation day conditions"""

    result = DataCalculationTask().calculating_data(city_data=city_data)
    assert type(result) == CityWeatherDayModel
    assert type(result.data[0]) == DayTempConditionModel
    assert result.data[0].date == '2022-05-26'
    assert result.data[0].day_average_temp == 17.7
    assert result.data[0].good_conditions_hours == 7


def test_calculating_final_results(calculated_data: CityWeatherDayModel):
    """Test for calculation final conditions"""

    result = DataCalculationTask().calculating_final_results(
        data=calculated_data
    )
    assert type(result) == FinalResultsModel
    assert result.city == 'MOSCOW'
    assert result.total_average_temp == 13.8
    assert result.total_good_conditions_hours == 8


def test_general_calculation(city_data: CityModel):
    """Test for general calculation data to FinalResultsModel"""

    result = DataCalculationTask().general_calculation(
        city_data=city_data
    )
    assert type(result) == FinalResultsModel
    assert city_data.city == result.city
    assert result.total_average_temp == 13.8
    assert result.total_good_conditions_hours == 8


def test_adding_rating_new():
    """Test for calculating rating and models"""

    forecasts = map(DataFetchingTask().make_request, CITIES.keys())
    data = map(
        DataCalculationTask().general_calculation, forecasts
    )
    result = DataCalculationTask().adding_rating(data)
    assert type(result) == RatingCityListModel
    assert type(result.cities[0]) == RatingCityModel
    assert type(result.cities[0].city) == FinalResultsModel
    assert result.cities[0].rating == 1


def test_save_results_to_json(data_for_result):
    """Test save final result to json"""

    DataAggregationTask.save_results_to_json(data_for_result)
    assert Path(RESULT_FILE).exists()


def test_get_result(data_for_result):
    """Test for get the best city by conditions in stdout"""

    data = (
        'The best weather condition in city ABUDHABI: average temperature 34.3 '
        'and 35 hours without bad weather conditions.'
    )
    result = DataAnalyzingTask().get_result(data_for_result)
    assert data == result
