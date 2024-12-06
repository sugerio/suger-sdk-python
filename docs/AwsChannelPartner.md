# AwsChannelPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The AWS Account ID of the Channel Partner | [optional] 
**name** | **str** | The name of the Channel Partner | [optional] 

## Example

```python
from suger_sdk_python.models.aws_channel_partner import AwsChannelPartner

# TODO update the JSON string below
json = "{}"
# create an instance of AwsChannelPartner from a JSON string
aws_channel_partner_instance = AwsChannelPartner.from_json(json)
# print the JSON string representation of the object
print(AwsChannelPartner.to_json())

# convert the object into a dict
aws_channel_partner_dict = aws_channel_partner_instance.to_dict()
# create an instance of AwsChannelPartner from a dict
aws_channel_partner_from_dict = AwsChannelPartner.from_dict(aws_channel_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


