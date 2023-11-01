# OrbPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_plan_id** | **str** | The parent plan id if the given plan was created by overriding one or more of the parent&#39;s prices. | [optional] 
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**default_invoice_memo** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**discount** | [**OrbPriceDiscount**](OrbPriceDiscount.md) |  | [optional] 
**external_plan_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invoicing_currency** | **str** |  | [optional] 
**maximum** | [**OrbPriceMaximum**](OrbPriceMaximum.md) |  | [optional] 
**metering_dimensions** | [**List[MeteringDimension]**](MeteringDimension.md) | The following fields are populated by Suger. The suger metering dimensions that are mapped to the orb billable metrics. | [optional] 
**minimum** | [**OrbPriceMinimum**](OrbPriceMinimum.md) |  | [optional] 
**name** | **str** |  | [optional] 
**net_terms** | **int** | Determines the difference between the invoice issue date and the due date. A value of \&quot;0\&quot; here signifies that invoices are due on issue, whereas a value of \&quot;30\&quot; means that the customer has a month to pay the invoice before its overdue. Note that individual subscriptions or invoices may set a different net terms configuration. | [optional] 
**plan_phases** | [**List[OrbPlanPhase]**](OrbPlanPhase.md) |  | [optional] 
**prices** | [**List[OrbPrice]**](OrbPrice.md) |  | [optional] 
**product** | [**OrbProduct**](OrbProduct.md) |  | [optional] 
**status** | [**OrbPlanStatus**](OrbPlanStatus.md) |  | [optional] 
**trial_config** | [**OrbTrialConfig**](OrbTrialConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.orb_plan import OrbPlan

# TODO update the JSON string below
json = "{}"
# create an instance of OrbPlan from a JSON string
orb_plan_instance = OrbPlan.from_json(json)
# print the JSON string representation of the object
print OrbPlan.to_json()

# convert the object into a dict
orb_plan_dict = orb_plan_instance.to_dict()
# create an instance of OrbPlan from a dict
orb_plan_form_dict = orb_plan.from_dict(orb_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


