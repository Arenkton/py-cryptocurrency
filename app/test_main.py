from pytest_mock import MockerFixture
from app.main import cryptocurrency_action


def test_predicted_exchange_rate_is_5positive(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=105)

    assert cryptocurrency_action(100) == "Do nothing"


def test_predicted_exchange_rate_is_5negative(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=95)

    assert cryptocurrency_action(100) == "Do nothing"


def test_predicted_difference_is_not_big(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=101)

    assert cryptocurrency_action(100) == "Do nothing"


def test_predicted_exchange_rate_is_more(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=106)

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


def test_predicted_exchange_rate_is_less(mocker: MockerFixture) -> None:
    mocker.patch("app.main.get_exchange_rate_prediction", return_value=94)

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"
