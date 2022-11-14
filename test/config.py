#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration """

    ## Azure Bot Service ##

    PORT = 8000
    APP_ID = os.environ.get("APP_ID", "")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "")
    
    ## Luis Service ##
    LUIS_APP_ID = os.environ.get("LUISAPPID", "2805db0b-a3d3-4708-9fd5-8b2388702701")
    LUIS_API_KEY = os.environ.get("LUISAPIKEY", "ee900aafeadf4cbe8a2b9571984bc2bb")
    LUIS_API_HOST_NAME = os.environ.get("LUIS_API_HOST_NAME", "westeurope.api.cognitive.microsoft.com")
    LUIS_API_ENDPOINT = os.environ.get("LUIS_API_ENDPOINT", "https://myflymebot.cognitiveservices.azure.com/")

    ## App Insight Service ##
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "APPINSIGHTSINSTRUMENTATIONKEY", "9d08958a-bc12-453b-80a2-10d03c0934fe")
    
    
   
