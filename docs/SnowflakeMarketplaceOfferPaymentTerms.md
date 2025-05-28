# SnowflakeMarketplaceOfferPaymentTerms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installment_schedule** | [**SnowflakeMarketplacePlanInstallmentSchedule**](SnowflakeMarketplacePlanInstallmentSchedule.md) | The installment schedule for the offer. | [optional] 
**payment_type** | **str** | The pricing plan payment types. Accepted values are INVOICE, CREDIT_CARD, INSTALLMENT. | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_offer_payment_terms import SnowflakeMarketplaceOfferPaymentTerms

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceOfferPaymentTerms from a JSON string
snowflake_marketplace_offer_payment_terms_instance = SnowflakeMarketplaceOfferPaymentTerms.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceOfferPaymentTerms.to_json())

# convert the object into a dict
snowflake_marketplace_offer_payment_terms_dict = snowflake_marketplace_offer_payment_terms_instance.to_dict()
# create an instance of SnowflakeMarketplaceOfferPaymentTerms from a dict
snowflake_marketplace_offer_payment_terms_from_dict = SnowflakeMarketplaceOfferPaymentTerms.from_dict(snowflake_marketplace_offer_payment_terms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


