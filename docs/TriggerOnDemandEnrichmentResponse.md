# TriggerOnDemandEnrichmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.trigger_on_demand_enrichment_response import TriggerOnDemandEnrichmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerOnDemandEnrichmentResponse from a JSON string
trigger_on_demand_enrichment_response_instance = TriggerOnDemandEnrichmentResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerOnDemandEnrichmentResponse.to_json())

# convert the object into a dict
trigger_on_demand_enrichment_response_dict = trigger_on_demand_enrichment_response_instance.to_dict()
# create an instance of TriggerOnDemandEnrichmentResponse from a dict
trigger_on_demand_enrichment_response_from_dict = TriggerOnDemandEnrichmentResponse.from_dict(trigger_on_demand_enrichment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


