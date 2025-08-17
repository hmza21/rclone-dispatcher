# Rclone Dispatcher

## Overview

This project provides a simple dispatcher script for managing [rclone](https://rclone.org/) operations. It helps automate mounting remote file systems using rclone, designed to be ran as a startup task.

## Features

- Easy configuration for multiple rclone tasks
- Simple command-line interface
- Logging of operations

## Requirements

- [rclone](https://rclone.org/) installed
- Bash or compatible shell

## Usage

1. Clone this repository.

1. Create a virtual environment using `venv`

    ```bash
    python3 -m venv venv
    ```

1. Activate the virtual environment.

    Linux and macOS:

    ```bash
    source venv/bin/activate
    ```

    Windows:

    ```bash
    .\venv\Scripts\activate
    ```

1. Install `requirements.txt` using `pip`.

    ```bash
    pip install -r requirements.txt
    ```

1. [Optional] You can now deactivate the virtual environment.

    Linux and macOS:

    ```bash
    deactivate
    ```

    Windows:

    ```bash
    .\venv\Scripts\deactivate
    ```

1. Copy `config_template.json` into `config.json` to configure your rclone tasks. The file is straightforward, just copy the following segment if you have multiple drives:

    ```json
    {
        "name": "<name>",
        "dir": "<directory>"
    },
    ```

1. Run the dispatcher script:

    ```bash
    ./rclone_dispatcher.sh
    ```

    or run the Python file directly:

    ```bash
    python3 main.py
    ```

    or register it as a startup script in your system.
