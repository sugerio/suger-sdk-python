# GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gmt_create** | **str** | example:  2023-01-11 10:31:00 | [optional] 
**metering_data** | [**List[ClientPushMeteringDataRequestMeteringData]**](ClientPushMeteringDataRequestMeteringData.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request import GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest from a JSON string
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request_instance = GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest.from_json(json)
# print the JSON string representation of the object
print(GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest.to_json())

# convert the object into a dict
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request_dict = github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request_instance.to_dict()
# create an instance of GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest from a dict
github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request_from_dict = GithubComAlibabacloudGoMarketplaceintl20221230ClientPushMeteringDataRequest.from_dict(github_com_alibabacloud_go_marketplaceintl20221230_client_push_metering_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


