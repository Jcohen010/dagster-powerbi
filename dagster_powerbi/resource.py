import datetime
import json
import logging
import time
from typing import Any, Mapping, Optional, Sequence, Tuple
from urllib.parse import urljoin

from dagster import (
    Failure,
    InitResourceContext,
    MetadataValue,
    __version__,
    _check as check,
    get_dagster_logger,
    resource,
)
from dagster._config.pythonic_config import ConfigurableResource
from dagster._core.definitions.resource_definition import dagster_maintained_resource
from dagster._utils.cached_method import cached_method
from dateutil import parser
from pydantic import Field
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

from pypowerbi import client

AUTHORITY_URL = 'https://login.windows.net/common'
RESOURCE_URL = 'https://analysis.windows.net/powerbi/api'
API_BASE_URL = 'https://api.powerbi.com'

class PowerBIResource(ConfigurableResource):
    """This class exposes methods ontop of the PowerBI REST API, which is leveraged through the use 
    of the pypowerbi python library"""

    client_id: str = Field(description="Client ID of PowerBI registered App in Azure")
    username: str = Field(description="PowerBI login username")
    password: str = Field(description="PowerBI login username")

    @property
    @cached_method
    def _log(self) -> logging.Logger:
        return get_dagster_logger()
    
    def get_datasets():
        pass
    
    def refresh_dataset():
        pass