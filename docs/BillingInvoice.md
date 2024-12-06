# BillingInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyer_id** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**entitlement_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BillingInvoiceInfo**](BillingInvoiceInfo.md) |  | [optional] 
**invoice_url** | **str** | The invoice file URL, provided as AWS S3 presigned URL with expiration time. Output only. | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**payment_status** | [**BillingPaymentStatus**](BillingPaymentStatus.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**status** | [**BillingInvoiceStatus**](BillingInvoiceStatus.md) |  | [optional] 
**type** | [**BillingInvoiceType**](BillingInvoiceType.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_invoice import BillingInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInvoice from a JSON string
billing_invoice_instance = BillingInvoice.from_json(json)
# print the JSON string representation of the object
print(BillingInvoice.to_json())

# convert the object into a dict
billing_invoice_dict = billing_invoice_instance.to_dict()
# create an instance of BillingInvoice from a dict
billing_invoice_from_dict = BillingInvoice.from_dict(billing_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


