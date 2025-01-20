# UpdateInvoiceInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **float** |  | [optional] 
**discount_type** | [**BillingDiscountType**](BillingDiscountType.md) | The overall discount of the invoice. | [optional] 
**due_date** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.update_invoice_info_request import UpdateInvoiceInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInvoiceInfoRequest from a JSON string
update_invoice_info_request_instance = UpdateInvoiceInfoRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInvoiceInfoRequest.to_json())

# convert the object into a dict
update_invoice_info_request_dict = update_invoice_info_request_instance.to_dict()
# create an instance of UpdateInvoiceInfoRequest from a dict
update_invoice_info_request_from_dict = UpdateInvoiceInfoRequest.from_dict(update_invoice_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


