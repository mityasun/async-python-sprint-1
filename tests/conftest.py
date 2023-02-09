import pytest

from models import CityModel, CityWeatherDayModel, RatingCityListModel


@pytest.fixture()
def city_data():
    model = {
        "city": "MOSCOW",
        "forecasts": {
            "forecasts": [
                {
                    "date": "2022-05-26",
                    "hours": [
                        {
                            "condition": "overcast",
                            "hour": 0,
                            "temp": 10
                        },
                        {
                            "condition": "overcast",
                            "hour": 1,
                            "temp": 10
                        },
                        {
                            "condition": "overcast",
                            "hour": 2,
                            "temp": 9
                        },
                        {
                            "condition": "overcast",
                            "hour": 3,
                            "temp": 8
                        },
                        {
                            "condition": "overcast",
                            "hour": 4,
                            "temp": 7
                        },
                        {
                            "condition": "overcast",
                            "hour": 5,
                            "temp": 8
                        },
                        {
                            "condition": "overcast",
                            "hour": 6,
                            "temp": 9
                        },
                        {
                            "condition": "cloudy",
                            "hour": 7,
                            "temp": 11
                        },
                        {
                            "condition": "cloudy",
                            "hour": 8,
                            "temp": 13
                        },
                        {
                            "condition": "cloudy",
                            "hour": 9,
                            "temp": 15
                        },
                        {
                            "condition": "cloudy",
                            "hour": 10,
                            "temp": 17
                        },
                        {
                            "condition": "cloudy",
                            "hour": 11,
                            "temp": 18
                        },
                        {
                            "condition": "cloudy",
                            "hour": 12,
                            "temp": 19
                        },
                        {
                            "condition": "overcast",
                            "hour": 13,
                            "temp": 20
                        },
                        {
                            "condition": "overcast",
                            "hour": 14,
                            "temp": 20
                        },
                        {
                            "condition": "overcast",
                            "hour": 15,
                            "temp": 19
                        },
                        {
                            "condition": "light-rain",
                            "hour": 16,
                            "temp": 18
                        },
                        {
                            "condition": "light-rain",
                            "hour": 17,
                            "temp": 17
                        },
                        {
                            "condition": "light-rain",
                            "hour": 18,
                            "temp": 17
                        },
                        {
                            "condition": "light-rain",
                            "hour": 19,
                            "temp": 15
                        },
                        {
                            "condition": "light-rain",
                            "hour": 20,
                            "temp": 14
                        },
                        {
                            "condition": "light-rain",
                            "hour": 21,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 22,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 23,
                            "temp": 12
                        }
                    ]
                },
                {
                    "date": "2022-05-27",
                    "hours": [
                        {
                            "condition": "light-rain",
                            "hour": 0,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 1,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 2,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 3,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 4,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 5,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 6,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 7,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 8,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 9,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 10,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 11,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 12,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 13,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 14,
                            "temp": 13
                        },
                        {
                            "condition": "showers",
                            "hour": 15,
                            "temp": 14
                        },
                        {
                            "condition": "showers",
                            "hour": 16,
                            "temp": 14
                        },
                        {
                            "condition": "showers",
                            "hour": 17,
                            "temp": 14
                        },
                        {
                            "condition": "light-rain",
                            "hour": 18,
                            "temp": 14
                        },
                        {
                            "condition": "light-rain",
                            "hour": 19,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 20,
                            "temp": 13
                        },
                        {
                            "condition": "cloudy",
                            "hour": 21,
                            "temp": 12
                        },
                        {
                            "condition": "cloudy",
                            "hour": 22,
                            "temp": 11
                        },
                        {
                            "condition": "cloudy",
                            "hour": 23,
                            "temp": 10
                        }
                    ]
                },
                {
                    "date": "2022-05-28",
                    "hours": [
                        {
                            "condition": "overcast",
                            "hour": 0,
                            "temp": 10
                        },
                        {
                            "condition": "overcast",
                            "hour": 1,
                            "temp": 10
                        },
                        {
                            "condition": "overcast",
                            "hour": 2,
                            "temp": 10
                        },
                        {
                            "condition": "light-rain",
                            "hour": 3,
                            "temp": 9
                        },
                        {
                            "condition": "light-rain",
                            "hour": 4,
                            "temp": 9
                        },
                        {
                            "condition": "light-rain",
                            "hour": 5,
                            "temp": 9
                        },
                        {
                            "condition": "light-rain",
                            "hour": 6,
                            "temp": 9
                        },
                        {
                            "condition": "light-rain",
                            "hour": 7,
                            "temp": 10
                        },
                        {
                            "condition": "showers",
                            "hour": 8,
                            "temp": 11
                        },
                        {
                            "condition": "showers",
                            "hour": 9,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 10,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 11,
                            "temp": 11
                        },
                        {
                            "condition": "light-rain",
                            "hour": 12,
                            "temp": 12
                        },
                        {
                            "condition": "showers",
                            "hour": 13,
                            "temp": 12
                        },
                        {
                            "condition": "showers",
                            "hour": 14,
                            "temp": 13
                        },
                        {
                            "condition": "showers",
                            "hour": 15,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 16,
                            "temp": 13
                        },
                        {
                            "condition": "showers",
                            "hour": 17,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 18,
                            "temp": 13
                        },
                        {
                            "condition": "light-rain",
                            "hour": 19,
                            "temp": 12
                        },
                        {
                            "condition": "light-rain",
                            "hour": 20,
                            "temp": 11
                        },
                        {
                            "condition": "cloudy",
                            "hour": 21,
                            "temp": 11
                        },
                        {
                            "condition": "cloudy",
                            "hour": 22,
                            "temp": 10
                        },
                        {
                            "condition": "cloudy",
                            "hour": 23,
                            "temp": 9
                        }
                    ]
                },
                {
                    "date": "2022-05-29",
                    "hours": [
                        {
                            "condition": "clear",
                            "hour": 0,
                            "temp": 9
                        },
                        {
                            "condition": "clear",
                            "hour": 1,
                            "temp": 8
                        },
                        {
                            "condition": "clear",
                            "hour": 2,
                            "temp": 8
                        },
                        {
                            "condition": "clear",
                            "hour": 3,
                            "temp": 8
                        },
                        {
                            "condition": "clear",
                            "hour": 4,
                            "temp": 7
                        },
                        {
                            "condition": "cloudy",
                            "hour": 5,
                            "temp": 8
                        },
                        {
                            "condition": "cloudy",
                            "hour": 6,
                            "temp": 9
                        },
                        {
                            "condition": "cloudy",
                            "hour": 7,
                            "temp": 10
                        },
                        {
                            "condition": "light-rain",
                            "hour": 8,
                            "temp": 11
                        },
                        {
                            "condition": "cloudy",
                            "hour": 9,
                            "temp": 12
                        }
                    ]
                },
                {
                    "date": "2022-05-30",
                    "hours": []
                }
            ]
        }
    }
    data = CityModel.parse_obj(model)
    return data


@pytest.fixture()
def calculated_data():
    data = {
        "city": "MOSCOW",
        "data":
            [
                {"date": "2022-05-26", "day_average_temp": 17.7,
                 "good_conditions_hours": 7},
                {"date": "2022-05-27", "day_average_temp": 13.1,
                 "good_conditions_hours": 0},
                {"date": "2022-05-28", "day_average_temp": 12.2,
                 "good_conditions_hours": 0},
                {"date": "2022-05-29", "day_average_temp": 12.0,
                 "good_conditions_hours": 1},
                {"date": "2022-05-30", "day_average_temp": 0.0,
                 "good_conditions_hours": 0}
            ]
    }
    data = CityWeatherDayModel.parse_obj(data)
    return data


@pytest.fixture()
def data_for_result():
    data = {
        "cities": [
            {
                "city": {
                    "city": "ABUDHABI",
                    "total_average_temp": 34.3,
                    "total_good_conditions_hours": 35
                },
                "rating": 1
            },
            {
                "city": {
                    "city": "CAIRO",
                    "total_average_temp": 33.4,
                    "total_good_conditions_hours": 33
                },
                "rating": 2
            },
            {
                "city": {
                    "city": "BEIJING",
                    "total_average_temp": 31.6,
                    "total_good_conditions_hours": 39
                },
                "rating": 3
            },
            {
                "city": {
                    "city": "ROMA",
                    "total_average_temp": 27.9,
                    "total_good_conditions_hours": 33
                },
                "rating": 4
            },
            {
                "city": {
                    "city": "BUCHAREST",
                    "total_average_temp": 24.9,
                    "total_good_conditions_hours": 34
                },
                "rating": 5
            },
            {
                "city": {
                    "city": "VOLGOGRAD",
                    "total_average_temp": 23.6,
                    "total_good_conditions_hours": 34
                },
                "rating": 6
            },
            {
                "city": {
                    "city": "NOVOSIBIRSK",
                    "total_average_temp": 23.2,
                    "total_good_conditions_hours": 38
                },
                "rating": 7
            },
            {
                "city": {
                    "city": "PARIS",
                    "total_average_temp": 17.3,
                    "total_good_conditions_hours": 31
                },
                "rating": 8
            },
            {
                "city": {
                    "city": "BERLIN",
                    "total_average_temp": 16.3,
                    "total_good_conditions_hours": 15
                },
                "rating": 9
            },
            {
                "city": {
                    "city": "LONDON",
                    "total_average_temp": 16.1,
                    "total_good_conditions_hours": 33
                },
                "rating": 10
            },
            {
                "city": {
                    "city": "WARSZAWA",
                    "total_average_temp": 15.5,
                    "total_good_conditions_hours": 14
                },
                "rating": 11
            },
            {
                "city": {
                    "city": "MOSCOW",
                    "total_average_temp": 13.8,
                    "total_good_conditions_hours": 8
                },
                "rating": 12
            },
            {
                "city": {
                    "city": "KAZAN",
                    "total_average_temp": 13.7,
                    "total_good_conditions_hours": 10
                },
                "rating": 13
            },
            {
                "city": {
                    "city": "KALININGRAD",
                    "total_average_temp": 13.3,
                    "total_good_conditions_hours": 12
                },
                "rating": 14
            },
            {
                "city": {
                    "city": "SPETERSBURG",
                    "total_average_temp": 11.9,
                    "total_good_conditions_hours": 4
                },
                "rating": 15
            }
        ]
    }
    data = RatingCityListModel.parse_obj(data)
    return data
