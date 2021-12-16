import covid_data_handler
import sched
import time


def test_parse_csv_data():
    """
    This test ensures parse_csv_data returns the correct number of results.
    """
    data = parse_csv_data('./resources/nation_2021-10-28.csv')
    assert len(data) == 639

def test_process_covid_csv_data():
    """
    This test ensures process_covid_csv_data correctly processes the csv data.
    """
    last7day_cases, current_hospital_cases, total_deaths = process_covid_csv_data(
        parse_csv_data('./resources/nation_2021-10-28.csv')
    )
    assert last7day_cases == 240_299
    assert current_hospital_cases == 7_019
    assert total_deaths == 141_544

def test_covid_API_request():
    data = covid_API_request()
    assert isinstance(data, dict)

def test_schedule_covid_updates():
    schedule_covid_updates(update_interval=10, update_name='update test')

def test_find_first_valid_entry():
    """
    This test ensures that find_first_valid_entry returns the index of the first
    value that is not None
    """
    test_data = [
        [None],
        [None],
        [True]
    ]

    result = find_first_valid_entry(test_data, 0)

    assert result == 2

def test_calculate_7_day_cases():
    """
    This test ensures that calculate_7_day_cases correctly calculates the cumulative
    cases in the last 7 days.
    """
    test_data = [
        {
            "newCasesBySpecimenDate": None
        },
        {
            "newCasesBySpecimenDate": -1
        },
        {
            "newCasesBySpecimenDate": 1
        },
        {
            "newCasesBySpecimenDate": 2
        },
        {
            "newCasesBySpecimenDate": 3
        },
        {
            "newCasesBySpecimenDate": 4
        },
        {
            "newCasesBySpecimenDate": 5
        },
        {
            "newCasesBySpecimenDate": 6
        },
        {
            "newCasesBySpecimenDate": 7
        },
    ]

    result = calculate_7_day_cases(test_data)

    assert result == 28


def test_create_wrapper():
    """
    This test ensures that the create wrapper function correctly
    removes the event from the array after the function has been run
    """
    reset_test_environment()

    function_called = False
    def test_function():
        nonlocal function_called

        function_called = True

    event = {
        "name": "Example Event"
    }

    scheduler.scheduled_updates.append(event)

    wrapper_function = scheduler.create_wrapper(test_function, event)

    wrapper_function()

    assert function_called is True
    assert len(scheduler.scheduled_updates) == 0

def test_cancel_task():
    """
    This test ensures that cancel_task will remove an event from the scheduled_updates list.
    """
    reset_test_environment()

    event_id = scheduler.scheduler.enter(0, 1, print)

    event = {
        "unique_identifier": 123456,
        "event": event_id
    }

    scheduler.scheduled_updates = [
        event
    ]

    result = scheduler.cancel_task(event)

    assert result is True

def test_cancel_task_failure():
    """
    This test ensures that cancel_task will return False if a ValueError is thrown
    """
    reset_test_environment()

    result = scheduler.cancel_task({
        "event": None
    })

    assert result is False

print("hello")