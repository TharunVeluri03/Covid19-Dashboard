# Covid19-Dashboard
Automatic covid dashboard for displaying accurate, up to date covid data and news.

## Table of Contents

 - [Features](#features)
 - [Config File](#config_file)
 - [Testing](#testing)
 - [How To Use Application](#How_To_Use_Application)
 - [Disclaimer](#Disclaimer)


## Features

- Display up-to-date COVID-19 statistics
  - Display both local and national articles
- Display recent news articles about the configured search terms
  - Remove articles from being displayed, even after new ones are fetched
- Schedule one-time and repeating updates to fetch new statistics and news articles
- All configurable

## Config File

This project has a configuration JSON file which can be used to customize the dashboard.

The default configuration is as follows:

```json
{
    "logging": {
        "enabled": true,
        "debug": false,
        "path": "./logging/log",
        "use_file": true,
        "dump_debug_on_error": true,
        "dump_debug_count": 10
    },

    "template": {
        "title": "COVID-19 UK Dashboard",
        "logo": "logo.webp",
        "favicon": "favicon.webp"
    },

    "location": "Exeter",
    "location_type": "ltla",
    "nation_location": "England",

    "search_terms": "Covid COVID-19 coronavirus",
    "language_code": "en",

    "news_api_key": "news-api-key",

    "resource_path": "./resources/",
    "static_path": "./static/",

    "inital_national_data_filename": "nation_2021-10-28.csv"
}
```

For the code to work please chage the required parameters to fit your need.
## Testing

This project uses pytest for its testing.  
All tests are inside the `/tests/` directory and have filenames according to the module it tests.
e.g. `test1_logger.py` for the `logger` module.  
  
### Running Tests

Running the tests is a simple task.  
Firstly ensure the `pytest` module is installed.  

    pip install pytest

After this, ensure you are in the root directory before running

    pytest

If this doesn't work try running `python -m pytest`

## How_To_Use_Application
When the website loads you will see three different sections.

In the centre of the dashboard you will see the local 7 day cases, national 7 day cases, hospital cases and total deaths( currently displays no values)

On the left hand side of the dashboard you will see the scheduled updates. When an update is scheduled then a title and and its description should be given.

On the right hand side you will see a list of news articles that when removed will not appear again.

## Disclaimer

Please note the website does not currently have any information dispalyed on it. However all functions within the code are working.
