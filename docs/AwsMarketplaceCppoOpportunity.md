# AwsMarketplaceCppoOpportunity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_ids** | **List[str]** | The AWS Account ID of buyer that are specified by the ISV/Seller in this CPPO Opportunity. | [optional] 
**buyer_names** | **List[str]** |  | [optional] 
**contract_duration_in_days** | **int** |  | [optional] 
**created_by** | **str** | The AWS Account ID of the ISV/Seller who create this CPPO Opportunity. | [optional] 
**created_date** | **str** | in format of \&quot;Wed Sep 13 17:50:07 UTC 2023\&quot; | [optional] 
**custom_price_terms** | [**AwsMarketplaceCppoPriceTerms**](AwsMarketplaceCppoPriceTerms.md) |  | [optional] 
**discount** | **str** | in format of \&quot;10.0\&quot; (10%) | [optional] 
**discount_percent** | **float** |  | [optional] 
**discount_type** | [**AwsMarketplaceCppoDiscountType**](AwsMarketplaceCppoDiscountType.md) |  | [optional] 
**errors** | **List[object]** |  | [optional] 
**expiration_date** | **str** | in format of \&quot;Thu Nov 30 23:59:59 UTC 2023\&quot; | [optional] 
**listing_fee_renewal** | **bool** |  | [optional] 
**manufacturer_id** | **str** | The AWS Account ID of the ISV/Seller | [optional] 
**manufacturer_name** | **str** | The name of the ISV/Seller | [optional] 
**offers_count** | **int** |  | [optional] 
**opportunity_discription** | **str** |  | [optional] 
**opportunity_duration_type** | [**AwsMarketplaceCppoDurationType**](AwsMarketplaceCppoDurationType.md) |  | [optional] 
**opportunity_eula** | [**AwsMarketplaceCppoOpportunityEula**](AwsMarketplaceCppoOpportunityEula.md) |  | [optional] 
**opportunity_id** | **str** |  | [optional] 
**opportunity_name** | **str** |  | [optional] 
**opportunity_rcmp** | [**AwsMarketplaceCppoOpportunityEula**](AwsMarketplaceCppoOpportunityEula.md) |  | [optional] 
**partner_id** | **str** | The AWS Account ID of the Channel Partner | [optional] 
**partner_name** | **str** | The name of the Channel Partner | [optional] 
**payment_terms** | [**AwsMarketplaceCppoPaymentTerms**](AwsMarketplaceCppoPaymentTerms.md) |  | [optional] 
**product_id** | **str** | The AWS Product ID from the ISV/Seller in this CPPO Opportunity. | [optional] 
**product_name** | **str** | The AWS Product Name from the ISV/Seller in this CPPO Opportunity. | [optional] 
**product_type** | **str** | The type of the AWS Product from the ISV/Seller in this CPPO Opportunity. | [optional] 
**sppo** | **bool** |  | [optional] 
**status** | **str** | The status of the CPPO Opportunity. | [optional] 
**usage_allowed** | **int** | How many times the CPPO Opportunity can be allowed to create CPPO Private Offer by the Channel Partner. | [optional] 

## Example

```python
from openapi_client.models.aws_marketplace_cppo_opportunity import AwsMarketplaceCppoOpportunity

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceCppoOpportunity from a JSON string
aws_marketplace_cppo_opportunity_instance = AwsMarketplaceCppoOpportunity.from_json(json)
# print the JSON string representation of the object
print AwsMarketplaceCppoOpportunity.to_json()

# convert the object into a dict
aws_marketplace_cppo_opportunity_dict = aws_marketplace_cppo_opportunity_instance.to_dict()
# create an instance of AwsMarketplaceCppoOpportunity from a dict
aws_marketplace_cppo_opportunity_form_dict = aws_marketplace_cppo_opportunity.from_dict(aws_marketplace_cppo_opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


