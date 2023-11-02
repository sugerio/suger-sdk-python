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
from pydantic import Field, StrictInt, StrictStr

from typing import Optional

from openapi_client.models.list_notification_messages_response import ListNotificationMessagesResponse
from openapi_client.models.notification_message import NotificationMessage

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NotificationApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_notification_message(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], notification_message_id : Annotated[StrictStr, Field(..., description="Notification Message ID")], **kwargs) -> NotificationMessage:  # noqa: E501
        """Get the notification message  # noqa: E501

        Get the notification message of the organization & notification message ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notification_message(org_id, notification_message_id, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param notification_message_id: Notification Message ID (required)
        :type notification_message_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NotificationMessage
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_notification_message_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_notification_message_with_http_info(org_id, notification_message_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_notification_message_with_http_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], notification_message_id : Annotated[StrictStr, Field(..., description="Notification Message ID")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get the notification message  # noqa: E501

        Get the notification message of the organization & notification message ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notification_message_with_http_info(org_id, notification_message_id, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param notification_message_id: Notification Message ID (required)
        :type notification_message_id: str
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
        :rtype: tuple(NotificationMessage, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'org_id',
            'notification_message_id'
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
                    " to method get_notification_message" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['org_id']:
            _path_params['orgId'] = _params['org_id']

        if _params['notification_message_id']:
            _path_params['notificationMessageId'] = _params['notification_message_id']


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
            '200': "NotificationMessage",
            '400': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/org/{orgId}/notificationMessage/{notificationMessageId}', 'GET',
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
    def list_notification_messages(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], limit : Annotated[Optional[StrictInt], Field(description="List pagination size, default 20, max value is 1000")] = None, offset : Annotated[Optional[StrictInt], Field(description="List pagination offset, default 0")] = None, **kwargs) -> ListNotificationMessagesResponse:  # noqa: E501
        """List the notification messages  # noqa: E501

        List the notification messages of the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_notification_messages(org_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param limit: List pagination size, default 20, max value is 1000
        :type limit: int
        :param offset: List pagination offset, default 0
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListNotificationMessagesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_notification_messages_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_notification_messages_with_http_info(org_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def list_notification_messages_with_http_info(self, org_id : Annotated[StrictStr, Field(..., description="Organization ID")], limit : Annotated[Optional[StrictInt], Field(description="List pagination size, default 20, max value is 1000")] = None, offset : Annotated[Optional[StrictInt], Field(description="List pagination offset, default 0")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List the notification messages  # noqa: E501

        List the notification messages of the organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_notification_messages_with_http_info(org_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param org_id: Organization ID (required)
        :type org_id: str
        :param limit: List pagination size, default 20, max value is 1000
        :type limit: int
        :param offset: List pagination offset, default 0
        :type offset: int
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
        :rtype: tuple(ListNotificationMessagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'org_id',
            'limit',
            'offset'
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
                    " to method list_notification_messages" % _key
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
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

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
            '200': "ListNotificationMessagesResponse",
            '400': "str",
            '500': "str",
        }

        return self.api_client.call_api(
            '/org/{orgId}/notificationMessage', 'GET',
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
