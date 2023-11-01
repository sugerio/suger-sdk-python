# OrbTrialConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_period** | **int** |  | [optional] 
**trial_period_unit** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_trial_config import OrbTrialConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OrbTrialConfig from a JSON string
orb_trial_config_instance = OrbTrialConfig.from_json(json)
# print the JSON string representation of the object
print OrbTrialConfig.to_json()

# convert the object into a dict
orb_trial_config_dict = orb_trial_config_instance.to_dict()
# create an instance of OrbTrialConfig from a dict
orb_trial_config_form_dict = orb_trial_config.from_dict(orb_trial_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


