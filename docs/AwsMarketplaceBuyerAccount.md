# AwsMarketplaceBuyerAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_account_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_buyer_account import AwsMarketplaceBuyerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceBuyerAccount from a JSON string
aws_marketplace_buyer_account_instance = AwsMarketplaceBuyerAccount.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceBuyerAccount.to_json())

# convert the object into a dict
aws_marketplace_buyer_account_dict = aws_marketplace_buyer_account_instance.to_dict()
# create an instance of AwsMarketplaceBuyerAccount from a dict
aws_marketplace_buyer_account_from_dict = AwsMarketplaceBuyerAccount.from_dict(aws_marketplace_buyer_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


