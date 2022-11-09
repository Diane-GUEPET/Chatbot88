#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Bot Configuration """

    ## Azure Bot Service ##

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    #49c63f45-161d-40ad-bf96-5839d2e7e595
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    #4f5a8008-ba00-476d-b552-328c7242cdb6
    ## Luis Service ##
    LUIS_APP_ID = os.environ.get("LuisAppId", "")
    #75e08333-d14c-4525-9925-25cf1499ac37
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "")
    #75ebbdac71964214897ee4a42a2958e1
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westeurope.api.cognitive.microsoft.com")
    LUIS_API_ENDPOINT = os.environ.get("LuisAPIEndPoint", "https://myflymebot.cognitiveservices.azure.com" )

    ## App Insight Service ##
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", ""
    )
    #9d08958a-bc12-453b-80a2-10d03c0934fe
    
   
