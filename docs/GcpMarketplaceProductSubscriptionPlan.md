# GcpMarketplaceProductSubscriptionPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | **str** | such as \&quot;ONE_YEAR\&quot;, \&quot;TWO_YEAR\&quot;, \&quot;THREE_YEAR\&quot; | [optional] 
**price** | [**GcpPriceValue**](GcpPriceValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_marketplace_product_subscription_plan import GcpMarketplaceProductSubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceProductSubscriptionPlan from a JSON string
gcp_marketplace_product_subscription_plan_instance = GcpMarketplaceProductSubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print GcpMarketplaceProductSubscriptionPlan.to_json()

# convert the object into a dict
gcp_marketplace_product_subscription_plan_dict = gcp_marketplace_product_subscription_plan_instance.to_dict()
# create an instance of GcpMarketplaceProductSubscriptionPlan from a dict
gcp_marketplace_product_subscription_plan_form_dict = gcp_marketplace_product_subscription_plan.from_dict(gcp_marketplace_product_subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


