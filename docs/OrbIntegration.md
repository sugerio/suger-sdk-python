# OrbIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The Bearer key to access the orb API. | [optional] 
**billable_metric_full_list** | [**List[OrbBillableMetric]**](OrbBillableMetric.md) |  | [optional] 
**billing_mode** | [**OrbBillingMode**](OrbBillingMode.md) |  | [optional] 
**enable_auto_report_usage** | **bool** | Whether to enable the auto usage report for the orb integration. If enabled, cron job runs every hour to fetch usage events from Orb to Suger as UsageRecordGroups. | [optional] 
**plan_full_list** | [**List[OrbPlan]**](OrbPlan.md) |  | [optional] 
**secret_key** | **str** | The secret key used to store the ApiKey in AWS Secret manager. For internal usage only. | [optional] 

## Example

```python
from openapi_client.models.orb_integration import OrbIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of OrbIntegration from a JSON string
orb_integration_instance = OrbIntegration.from_json(json)
# print the JSON string representation of the object
print OrbIntegration.to_json()

# convert the object into a dict
orb_integration_dict = orb_integration_instance.to_dict()
# create an instance of OrbIntegration from a dict
orb_integration_form_dict = orb_integration.from_dict(orb_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


