# GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | example:  200 | [optional] 
**dynamic_message** | **str** | example:  parameter \\\\\&quot;service\\\\\&quot; can not be blank. | [optional] 
**force_fatal** | **bool** | example:  false | [optional] 
**message** | **str** | example:  Instance 5723f7ee-952d-411f-94f4-b942a550d9b8 does not exist. | [optional] 
**request_id** | **str** | example:  A6A33748-D573-593C-A3BC-593E33D68311 | [optional] 
**result** | **bool** | example:  True | [optional] 
**success** | **bool** | example:  True | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body import GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody from a JSON string
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body_instance = GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody.from_json(json)
# print the JSON string representation of the object
print(GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody.to_json())

# convert the object into a dict
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body_dict = github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body_instance.to_dict()
# create an instance of GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody from a dict
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body_from_dict = GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataResponseBody.from_dict(github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


