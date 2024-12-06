# AwsMarketplaceAgreementV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance_time** | **datetime** |  | [optional] 
**agreement_id** | **str** | AWS Marketplace Agreement Id | [optional] 
**agreement_type** | **str** |  | [optional] 
**buyer_account_id** | **str** | The AWS Account Id of the buyer in AWS Marketplace | [optional] 
**end_time** | **datetime** |  | [optional] 
**offer_id** | **str** | AWS Marketplace Offer Id | [optional] 
**product_id** | **str** | AWS Marketplace Product Id | [optional] 
**product_type** | **str** |  | [optional] 
**seller_account_id** | **str** | The AWS Account Id of the seller in AWS Marketplace | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | [**AwsMarketplaceAgreementStatus**](AwsMarketplaceAgreementStatus.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_agreement_v2 import AwsMarketplaceAgreementV2

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceAgreementV2 from a JSON string
aws_marketplace_agreement_v2_instance = AwsMarketplaceAgreementV2.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceAgreementV2.to_json())

# convert the object into a dict
aws_marketplace_agreement_v2_dict = aws_marketplace_agreement_v2_instance.to_dict()
# create an instance of AwsMarketplaceAgreementV2 from a dict
aws_marketplace_agreement_v2_from_dict = AwsMarketplaceAgreementV2.from_dict(aws_marketplace_agreement_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


