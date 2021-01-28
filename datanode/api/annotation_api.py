# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from datanode.api_client import ApiClient
from datanode.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AnnotationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_annotation(self, dataset_id, annotation_store_id, **kwargs):  # noqa: E501
        """Create an annotation  # noqa: E501

        Create an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation(dataset_id, annotation_store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param AnnotationCreateRequest annotation_create_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnotationCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_annotation_with_http_info(dataset_id, annotation_store_id, **kwargs)  # noqa: E501

    def create_annotation_with_http_info(self, dataset_id, annotation_store_id, **kwargs):  # noqa: E501
        """Create an annotation  # noqa: E501

        Create an annotation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_with_http_info(dataset_id, annotation_store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param AnnotationCreateRequest annotation_create_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnotationCreateResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dataset_id',
            'annotation_store_id',
            'annotation_create_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_annotation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dataset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dataset_id` when calling `create_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_store_id' is set
        if self.api_client.client_side_validation and ('annotation_store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_store_id` when calling `create_annotation`")  # noqa: E501

        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `create_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `create_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'dataset_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['dataset_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `create_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `create_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `create_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'annotation_store_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['annotation_store_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `create_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['datasetId'] = local_var_params['dataset_id']  # noqa: E501
        if 'annotation_store_id' in local_var_params:
            path_params['annotationStoreId'] = local_var_params['annotation_store_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'annotation_create_request' in local_var_params:
            body_params = local_var_params['annotation_create_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_annotation(self, dataset_id, annotation_store_id, annotation_id, **kwargs):  # noqa: E501
        """Delete an annotation  # noqa: E501

        Deletes the annotation specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation(dataset_id, annotation_store_id, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param str annotation_id: The ID of the annotation (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_annotation_with_http_info(dataset_id, annotation_store_id, annotation_id, **kwargs)  # noqa: E501

    def delete_annotation_with_http_info(self, dataset_id, annotation_store_id, annotation_id, **kwargs):  # noqa: E501
        """Delete an annotation  # noqa: E501

        Deletes the annotation specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation_with_http_info(dataset_id, annotation_store_id, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param str annotation_id: The ID of the annotation (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dataset_id',
            'annotation_store_id',
            'annotation_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_annotation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dataset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dataset_id` when calling `delete_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_store_id' is set
        if self.api_client.client_side_validation and ('annotation_store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_store_id` when calling `delete_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if self.api_client.client_side_validation and ('annotation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_id` when calling `delete_annotation`")  # noqa: E501

        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `delete_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `delete_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'dataset_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['dataset_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `delete_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `delete_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `delete_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'annotation_store_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['annotation_store_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `delete_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['datasetId'] = local_var_params['dataset_id']  # noqa: E501
        if 'annotation_store_id' in local_var_params:
            path_params['annotationStoreId'] = local_var_params['annotation_store_id']  # noqa: E501
        if 'annotation_id' in local_var_params:
            path_params['annotationId'] = local_var_params['annotation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_annotation(self, dataset_id, annotation_store_id, annotation_id, **kwargs):  # noqa: E501
        """Get an annotation  # noqa: E501

        Returns the annotation specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation(dataset_id, annotation_store_id, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param str annotation_id: The ID of the annotation (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Annotation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_annotation_with_http_info(dataset_id, annotation_store_id, annotation_id, **kwargs)  # noqa: E501

    def get_annotation_with_http_info(self, dataset_id, annotation_store_id, annotation_id, **kwargs):  # noqa: E501
        """Get an annotation  # noqa: E501

        Returns the annotation specified  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation_with_http_info(dataset_id, annotation_store_id, annotation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param str annotation_id: The ID of the annotation (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Annotation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dataset_id',
            'annotation_store_id',
            'annotation_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dataset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dataset_id` when calling `get_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_store_id' is set
        if self.api_client.client_side_validation and ('annotation_store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_store_id` when calling `get_annotation`")  # noqa: E501
        # verify the required parameter 'annotation_id' is set
        if self.api_client.client_side_validation and ('annotation_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_id` when calling `get_annotation`")  # noqa: E501

        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `get_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `get_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'dataset_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['dataset_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `get_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `get_annotation`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `get_annotation`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'annotation_store_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['annotation_store_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `get_annotation`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['datasetId'] = local_var_params['dataset_id']  # noqa: E501
        if 'annotation_store_id' in local_var_params:
            path_params['annotationStoreId'] = local_var_params['annotation_store_id']  # noqa: E501
        if 'annotation_id' in local_var_params:
            path_params['annotationId'] = local_var_params['annotation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations/{annotationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Annotation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_annotations(self, dataset_id, annotation_store_id, **kwargs):  # noqa: E501
        """List the annotations in an annotation store  # noqa: E501

        Returns the annotations in an annotation store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotations(dataset_id, annotation_store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param int limit: Maximum number of results returned
        :param int offset: Index of the first result that must be returned
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PageOfAnnotations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_annotations_with_http_info(dataset_id, annotation_store_id, **kwargs)  # noqa: E501

    def list_annotations_with_http_info(self, dataset_id, annotation_store_id, **kwargs):  # noqa: E501
        """List the annotations in an annotation store  # noqa: E501

        Returns the annotations in an annotation store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_annotations_with_http_info(dataset_id, annotation_store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str dataset_id: The ID of the dataset (required)
        :param str annotation_store_id: The ID of the annotation store (required)
        :param int limit: Maximum number of results returned
        :param int offset: Index of the first result that must be returned
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PageOfAnnotations, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'dataset_id',
            'annotation_store_id',
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_annotations" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'dataset_id' is set
        if self.api_client.client_side_validation and ('dataset_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['dataset_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `dataset_id` when calling `list_annotations`")  # noqa: E501
        # verify the required parameter 'annotation_store_id' is set
        if self.api_client.client_side_validation and ('annotation_store_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['annotation_store_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `annotation_store_id` when calling `list_annotations`")  # noqa: E501

        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `list_annotations`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('dataset_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['dataset_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `list_annotations`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'dataset_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['dataset_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `dataset_id` when calling `list_annotations`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) > 60):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `list_annotations`, length must be less than or equal to `60`")  # noqa: E501
        if self.api_client.client_side_validation and ('annotation_store_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['annotation_store_id']) < 3):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `list_annotations`, length must be greater than or equal to `3`")  # noqa: E501
        if self.api_client.client_side_validation and 'annotation_store_id' in local_var_params and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', local_var_params['annotation_store_id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `annotation_store_id` when calling `list_annotations`, must conform to the pattern `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_annotations`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 10:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_annotations`, must be a value greater than or equal to `10`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `list_annotations`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'dataset_id' in local_var_params:
            path_params['datasetId'] = local_var_params['dataset_id']  # noqa: E501
        if 'annotation_store_id' in local_var_params:
            path_params['annotationStoreId'] = local_var_params['annotation_store_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/annotationStores/{annotationStoreId}/annotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageOfAnnotations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
