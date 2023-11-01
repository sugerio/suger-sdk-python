# OrbBillableMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**OrbBillableMetricStatus**](OrbBillableMetricStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.orb_billable_metric import OrbBillableMetric

# TODO update the JSON string below
json = "{}"
# create an instance of OrbBillableMetric from a JSON string
orb_billable_metric_instance = OrbBillableMetric.from_json(json)
# print the JSON string representation of the object
print OrbBillableMetric.to_json()

# convert the object into a dict
orb_billable_metric_dict = orb_billable_metric_instance.to_dict()
# create an instance of OrbBillableMetric from a dict
orb_billable_metric_form_dict = orb_billable_metric.from_dict(orb_billable_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


