# AwsMarketplaceMeteringTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | One part of a key-value pair that makes up a tag. A key is a label that acts like a category for the specific tag values. | [optional] 
**value** | **str** | One part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_metering_tag import AwsMarketplaceMeteringTag

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceMeteringTag from a JSON string
aws_marketplace_metering_tag_instance = AwsMarketplaceMeteringTag.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceMeteringTag.to_json())

# convert the object into a dict
aws_marketplace_metering_tag_dict = aws_marketplace_metering_tag_instance.to_dict()
# create an instance of AwsMarketplaceMeteringTag from a dict
aws_marketplace_metering_tag_from_dict = AwsMarketplaceMeteringTag.from_dict(aws_marketplace_metering_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


