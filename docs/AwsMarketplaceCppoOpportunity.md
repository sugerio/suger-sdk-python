# AwsMarketplaceCppoOpportunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**dimensions** | [**List[AwsProductDimension]**](AwsProductDimension.md) |  | [optional] 
**manufacturer_account_id** | **str** |  | [optional] 
**manufacturer_legal_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offer_details** | [**AwsMarketplaceCppoOpportunityOfferDetails**](AwsMarketplaceCppoOpportunityOfferDetails.md) |  | [optional] 
**pre_existing_buyer_agreement** | [**AwsMarketplacePreExistingAgreement**](AwsMarketplacePreExistingAgreement.md) |  | [optional] 
**product_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**rules** | [**List[AwsMarketplaceCppoOpportunityRule]**](AwsMarketplaceCppoOpportunityRule.md) |  | [optional] 
**status** | **str** |  | [optional] 
**terms** | [**List[AwsMarketplaceCppoOpportunityTerm]**](AwsMarketplaceCppoOpportunityTerm.md) |  | [optional] 
**discount_type** | [**AwsMarketplaceCppoDiscountType**](AwsMarketplaceCppoDiscountType.md) | The following fields are not from aws catalog API, only used for cppo_out offer create. They shouldn&#39;t be read in other places because they will absent when fetch opportunity from aws catalog API. | [optional] 
**opportunity_duration_type** | [**AwsMarketplaceCppoDurationType**](AwsMarketplaceCppoDurationType.md) |  | [optional] 
**opportunity_id** | **str** |  | [optional] 
**partner_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_cppo_opportunity import AwsMarketplaceCppoOpportunity

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunity from a JSON string
aws_marketplace_cppo_opportunity_instance = AwsMarketplaceCppoOpportunity.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceCppoOpportunity.to_json())

# convert the object into a dict
aws_marketplace_cppo_opportunity_dict = aws_marketplace_cppo_opportunity_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunity from a dict
aws_marketplace_cppo_opportunity_from_dict = AwsMarketplaceCppoOpportunity.from_dict(aws_marketplace_cppo_opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


