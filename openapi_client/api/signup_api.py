# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictStr

from openapi_client.models.client_signup_page_config_info import ClientSignupPageConfigInfo

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SignupApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_client_signup_page_config_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], **kwargs) -> ClientSignupPageConfigInfo:  # noqa: E501
        """get client signup page config info  # noqa: E501

        Get the client signup page config info of the given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_client_signup_page_config_info(org_id, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClientSignupPageConfigInfo
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_client_signup_page_config_info_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_client_signup_page_config_info_with_http_info(org_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_client_signup_page_config_info_with_http_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """get client signup page config info  # noqa: E501

        Get the client signup page config info of the given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_client_signup_page_config_info_with_http_info(org_id, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClientSignupPageConfigInfo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'org_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client_signup_page_config_info" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['org_id']:
            _path_params['orgId'] = _params['org_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['BearerTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "ClientSignupPageConfigInfo",
            '400': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/org/{orgId}/clientSignupPageConfigInfo', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_client_signup_page_config_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], data : Annotated[ClientSignupPageConfigInfo, Field(..., description="The client signup page config info to update with")], **kwargs) -> ClientSignupPageConfigInfo:  # noqa: E501
        """update client signup page config info  # noqa: E501

        Update the client signup page config info of the given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_client_signup_page_config_info(org_id, data, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param data: The client signup page config info to update with (required)
        :type data: ClientSignupPageConfigInfo
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ClientSignupPageConfigInfo
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the update_client_signup_page_config_info_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.update_client_signup_page_config_info_with_http_info(org_id, data, **kwargs)  # noqa: E501

    @validate_arguments
    def update_client_signup_page_config_info_with_http_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], data : Annotated[ClientSignupPageConfigInfo, Field(..., description="The client signup page config info to update with")], **kwargs) -> ApiResponse:  # noqa: E501
        """update client signup page config info  # noqa: E501

        Update the client signup page config info of the given organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_client_signup_page_config_info_with_http_info(org_id, data, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param data: The client signup page config info to update with (required)
        :type data: ClientSignupPageConfigInfo
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ClientSignupPageConfigInfo, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'org_id',
            'data'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_client_signup_page_config_info" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['org_id']:
            _path_params['orgId'] = _params['org_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['data'] is not None:
            _body_params = _params['data']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['BearerTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "ClientSignupPageConfigInfo",
            '400': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/org/{orgId}/clientSignupPageConfigInfo', 'PATCH',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
