# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v2alpha1_pods_metric_source import V2alpha1PodsMetricSource


class TestV2alpha1PodsMetricSource(unittest.TestCase):
    """ V2alpha1PodsMetricSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1PodsMetricSource(self):
        """
        Test V2alpha1PodsMetricSource
        """
        model = kubernetes.client.models.v2alpha1_pods_metric_source.V2alpha1PodsMetricSource()


if __name__ == '__main__':
    unittest.main()
