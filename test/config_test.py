#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

class TestConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("APP_ID", "")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "")
    LUIS_APP_ID = os.environ.get("LUISAPPID", "")
    LUIS_API_KEY = os.environ.get("LUISAPIKEY", "")
    LUIS_API_HOST_NAME = os.environ.get("LUIS_API_HOST_NAME", "")
    LUIS_API_ENDPOINT = os.environ.get("LUIS_API_ENDPOINT", "")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "APPINSIGHTSINSTRUMENTATIONKEY", "")
