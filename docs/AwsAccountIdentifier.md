# AwsAccountIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account_id** | **str** | The AWS Account ID of the buyer in AWS Marketplace | [optional] 
**aws_customer_id** | **str** | The AWS Customer ID of the buyer in AWS Marketplace | [optional] 
**data_feed_account_id** | **str** | The Account ID in AWS Marketplace Data Feed service | [optional] 

## Example

```python
from suger_sdk_python.models.aws_account_identifier import AwsAccountIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAccountIdentifier from a JSON string
aws_account_identifier_instance = AwsAccountIdentifier.from_json(json)
# print the JSON string representation of the object
print(AwsAccountIdentifier.to_json())

# convert the object into a dict
aws_account_identifier_dict = aws_account_identifier_instance.to_dict()
# create an instance of AwsAccountIdentifier from a dict
aws_account_identifier_from_dict = AwsAccountIdentifier.from_dict(aws_account_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


