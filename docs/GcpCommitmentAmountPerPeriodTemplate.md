# GcpCommitmentAmountPerPeriodTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** |  | [optional] 
**decimal_amount_constraint** | [**GcpAmountConstraint**](GcpAmountConstraint.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_commitment_amount_per_period_template import GcpCommitmentAmountPerPeriodTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCommitmentAmountPerPeriodTemplate from a JSON string
gcp_commitment_amount_per_period_template_instance = GcpCommitmentAmountPerPeriodTemplate.from_json(json)
# print the JSON string representation of the object
print(GcpCommitmentAmountPerPeriodTemplate.to_json())

# convert the object into a dict
gcp_commitment_amount_per_period_template_dict = gcp_commitment_amount_per_period_template_instance.to_dict()
# create an instance of GcpCommitmentAmountPerPeriodTemplate from a dict
gcp_commitment_amount_per_period_template_from_dict = GcpCommitmentAmountPerPeriodTemplate.from_dict(gcp_commitment_amount_per_period_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


