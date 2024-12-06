# TrialConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trial_period** | **int** |  | [optional] 
**trial_period_unit** | [**TimeUnit**](TimeUnit.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.trial_config import TrialConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TrialConfig from a JSON string
trial_config_instance = TrialConfig.from_json(json)
# print the JSON string representation of the object
print(TrialConfig.to_json())

# convert the object into a dict
trial_config_dict = trial_config_instance.to_dict()
# create an instance of TrialConfig from a dict
trial_config_from_dict = TrialConfig.from_dict(trial_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


