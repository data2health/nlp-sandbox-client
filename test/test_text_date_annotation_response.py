"""
    NLP Sandbox Date Annotator API

    # Overview The OpenAPI specification implemented by NLP Sandbox Annotators.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import annotator
from annotator.model.text_date_annotation import TextDateAnnotation
globals()['TextDateAnnotation'] = TextDateAnnotation
from annotator.model.text_date_annotation_response import TextDateAnnotationResponse


class TestTextDateAnnotationResponse(unittest.TestCase):
    """TextDateAnnotationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTextDateAnnotationResponse(self):
        """Test TextDateAnnotationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TextDateAnnotationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
