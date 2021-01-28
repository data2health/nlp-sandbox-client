# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import datanode
from datanode.api.health_check_api import HealthCheckApi  # noqa: E501
from datanode.rest import ApiException


class TestHealthCheckApi(unittest.TestCase):
    """HealthCheckApi unit test stubs"""

    def setUp(self):
        self.api = datanode.api.health_check_api.HealthCheckApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_health_check(self):
        """Test case for get_health_check

        Get health check information  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
