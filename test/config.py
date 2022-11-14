#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration """

    ## Azure Bot Service ##

    PORT = 8000
    APP_ID = os.environ.get("APP_ID", "49c63f45-161d-40ad-bf96-5839d2e7e595")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "4f5a8008-ba00-476d-b552-328c7242cdb6")
    
    ## Luis Service ##
    LUIS_APP_ID = os.environ.get("LUISAPPID", "7a937442-e53c-4ad8-8bd6-db1e766c721c")
    LUIS_API_KEY = os.environ.get("LUISAPIKEY", "5fbcaf962489475a84324f147845851b")
    LUIS_API_HOST_NAME = os.environ.get("LUIS_API_HOST_NAME", "westeurope.api.cognitive.microsoft.com")
    LUIS_API_ENDPOINT = os.environ.get("LUIS_API_ENDPOINT", "https://myflymebot.cognitiveservices.azure.com/")

    ## App Insight Service ##
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "APPINSIGHTSINSTRUMENTATIONKEY", "9d08958a-bc12-453b-80a2-10d03c0934fe")
    
    
   
