# File System Browser

## Overview

This application takes in a file system location, and creates a REST API to access information on the contents at that location.

## Contents

It consists of an entrypoint bash script, `fs_browser.sh`, which prompts for a location. Then it will mount that location onto a Docker container, which contains a Flask application providing an API. Currently the API supports calls to GET filepaths within the original location.

## Running the application

To run the application, invoke the `fs_browser.sh` script and follow the prompts. Then, navigate to `localhost:3005` to begin browsing data.

## Testing

To run tests, this application utilizes the Pytest framework. Tests live inside `app/test_fs_browser.py`. Simply invoke the `pytest` command in the `fs_browser` folder to run them.