# GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering** | **str** | example:  [{\&quot;InstanceId\&quot;:\&quot;1000001\&quot;,\&quot;StartTime\&quot;:\&quot;100000000\&quot;,\&quot;EndTime\&quot;:\&quot;100000010\&quot;,\&quot;Entities\&quot;:[{\&quot;Key\&quot;:\&quot;PeriodMin\&quot;,\&quot;Value\&quot;:\&quot;96\&quot;,\&quot;meteringAssit\&quot;:\&quot;cmapi00060317-PeriodMin-4\&quot;}]}] | [optional] 

## Example

```python
from suger_sdk_python.models.github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request import GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest from a JSON string
github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request_instance = GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest.from_json(json)
# print the JSON string representation of the object
print(GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest.to_json())

# convert the object into a dict
github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request_dict = github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request_instance.to_dict()
# create an instance of GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest from a dict
github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request_from_dict = GithubComAlibabacloudGoMarket20151101V3ClientPushMeteringDataRequest.from_dict(github_com_alibabacloud_go_market20151101_v3_client_push_metering_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


