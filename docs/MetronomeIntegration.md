# MetronomeIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | The Bearer token for the metronome API. Required only when the metronome integration is created or updated with new API token. | [optional] 
**billable_metric_full_list** | [**List[MetronomeBillableMetric]**](MetronomeBillableMetric.md) | The full list of billable metrics fetched from metronome API for the available metronome customers. | [optional] 
**billable_metric_whitelist** | [**List[MetronomeBillableMetric]**](MetronomeBillableMetric.md) | The whitelist of billable metrics. Only the metrics in the whitelist will be metered &amp; reported to cloud marketplace. | [optional] 
**billing_mode** | [**MetronomeBillingMode**](MetronomeBillingMode.md) |  | [optional] 
**enable_auto_report_usage** | **bool** | Whether to enable the auto usage report for the metronome integration. If enabled, cron job runs every hour to fetch usage events from Metronome to Suger as UsageRecordGroups. | [optional] 
**enable_billable_metric_whitelist** | **bool** | Enable whitelist for billable metrics. If enabled, only the metrics in the whitelist will be metered &amp; reported to cloud marketplace. Otherwise all the metrics in the billableMetricFullList will be metered &amp; reported to cloud marketplace. | [optional] 
**secret_key** | **str** | The secret key used to store the ApiToken in AWS Secret manager. For internal usage only. | [optional] 

## Example

```python
from openapi_client.models.metronome_integration import MetronomeIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of MetronomeIntegration from a JSON string
metronome_integration_instance = MetronomeIntegration.from_json(json)
# print the JSON string representation of the object
print MetronomeIntegration.to_json()

# convert the object into a dict
metronome_integration_dict = metronome_integration_instance.to_dict()
# create an instance of MetronomeIntegration from a dict
metronome_integration_form_dict = metronome_integration.from_dict(metronome_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


