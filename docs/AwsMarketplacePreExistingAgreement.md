# AwsMarketplacePreExistingAgreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisition_channel** | [**AwsRenewalOfferType**](AwsRenewalOfferType.md) | Indicates if the existing agreement was signed outside AWS Marketplace or within AWS Marketplace. one of values [\&quot;External\&quot;, \&quot;AwsMarketplace\&quot;] | [optional] 
**pricing_model** | [**AwsMarketplaceCatalogPricingModel**](AwsMarketplaceCatalogPricingModel.md) | Indicates which pricing model the existing agreement uses. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_pre_existing_agreement import AwsMarketplacePreExistingAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplacePreExistingAgreement from a JSON string
aws_marketplace_pre_existing_agreement_instance = AwsMarketplacePreExistingAgreement.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplacePreExistingAgreement.to_json())

# convert the object into a dict
aws_marketplace_pre_existing_agreement_dict = aws_marketplace_pre_existing_agreement_instance.to_dict()
# create an instance of AwsMarketplacePreExistingAgreement from a dict
aws_marketplace_pre_existing_agreement_from_dict = AwsMarketplacePreExistingAgreement.from_dict(aws_marketplace_pre_existing_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


