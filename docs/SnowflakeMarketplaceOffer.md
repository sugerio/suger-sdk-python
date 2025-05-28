# SnowflakeMarketplaceOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_end_time** | **str** |  | [optional] 
**access_start_date_preference** | **str** |  | [optional] 
**access_start_time** | **str** |  | [optional] 
**additional_information** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**contract_duration_months** | **int** |  | [optional] 
**contract_type** | **str** |  | [optional] 
**contract_value** | **str** |  | [optional] 
**discount** | **float** |  | [optional] 
**display_name** | **str** |  | [optional] 
**expiration_time** | **str** |  | [optional] 
**invoice_start_date_preference** | **str** | invoice start date preference: FIRST_DAY_NEXT_MONTH, OFFER_ACCEPTED_DATE | [optional] 
**invoice_start_time** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**payment_terms** | [**SnowflakeMarketplaceOfferPaymentTerms**](SnowflakeMarketplaceOfferPaymentTerms.md) |  | [optional] 
**pricing_plan_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_updated_on** | **str** |  | [optional] 
**target_consumer** | **str** |  | [optional] 
**terms_of_service** | [**SnowflakeMarketplaceOfferTermsOfService**](SnowflakeMarketplaceOfferTermsOfService.md) | terms of service: {\&quot;type\&quot;:\&quot;DEFAULT\&quot;} | [optional] 
**updated_on** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.snowflake_marketplace_offer import SnowflakeMarketplaceOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeMarketplaceOffer from a JSON string
snowflake_marketplace_offer_instance = SnowflakeMarketplaceOffer.from_json(json)
# print the JSON string representation of the object
print(SnowflakeMarketplaceOffer.to_json())

# convert the object into a dict
snowflake_marketplace_offer_dict = snowflake_marketplace_offer_instance.to_dict()
# create an instance of SnowflakeMarketplaceOffer from a dict
snowflake_marketplace_offer_from_dict = SnowflakeMarketplaceOffer.from_dict(snowflake_marketplace_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


