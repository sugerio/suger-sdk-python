# MetronomeBillableMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **List[str]** | the fields to group by when aggregating usage events. | [optional] 
**id** | **str** | the uuid of the billable metric. | [optional] 
**name** | **str** | the name of the billable metric. | [optional] 

## Example

```python
from openapi_client.models.metronome_billable_metric import MetronomeBillableMetric

# TODO update the JSON string below
json = "{}"
# create an instance of MetronomeBillableMetric from a JSON string
metronome_billable_metric_instance = MetronomeBillableMetric.from_json(json)
# print the JSON string representation of the object
print MetronomeBillableMetric.to_json()

# convert the object into a dict
metronome_billable_metric_dict = metronome_billable_metric_instance.to_dict()
# create an instance of MetronomeBillableMetric from a dict
metronome_billable_metric_form_dict = metronome_billable_metric.from_dict(metronome_billable_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


