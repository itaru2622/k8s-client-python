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
from kubernetes.client.models.v1_namespace_spec import V1NamespaceSpec


class TestV1NamespaceSpec(unittest.TestCase):
    """ V1NamespaceSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1NamespaceSpec(self):
        """
        Test V1NamespaceSpec
        """
        model = kubernetes.client.models.v1_namespace_spec.V1NamespaceSpec()


if __name__ == '__main__':
    unittest.main()
