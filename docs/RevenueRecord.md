# RevenueRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The revenue amount for the revenue report | [optional] 
**buyer_id** | **str** |  | [optional] 
**collectable_amount** | **float** | The revenue amount that the seller/ISV can collect. | [optional] 
**currency** | **str** | The currency of the revenue in ISO 4217 format, such as \&quot;USD\&quot;. | [optional] 
**var_date** | **datetime** | The date for the revenue report | [optional] 
**disburse_amount** | **float** |  | [optional] 
**disburse_date** | **datetime** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**RevenueRecordInfo**](RevenueRecordInfo.md) |  | [optional] 
**invoice_amount** | **float** |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**payment_due_date** | **datetime** |  | [optional] 
**product_id** | **str** |  | [optional] 
**refund_disburse_amount** | **float** |  | [optional] 
**refund_disburse_date** | **datetime** |  | [optional] 
**refund_invoice_amount** | **float** |  | [optional] 
**refund_invoice_date** | **datetime** |  | [optional] 
**tax_amount** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.revenue_record import RevenueRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueRecord from a JSON string
revenue_record_instance = RevenueRecord.from_json(json)
# print the JSON string representation of the object
print RevenueRecord.to_json()

# convert the object into a dict
revenue_record_dict = revenue_record_instance.to_dict()
# create an instance of RevenueRecord from a dict
revenue_record_form_dict = revenue_record.from_dict(revenue_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


