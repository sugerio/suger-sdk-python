# StripeRefundDestinationDetailsUSBankTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | The reference assigned to the refund. | [optional] 
**reference_status** | **str** | Status of the reference on the refund. This can be &#x60;pending&#x60;, &#x60;available&#x60; or &#x60;unavailable&#x60;. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_refund_destination_details_us_bank_transfer import StripeRefundDestinationDetailsUSBankTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of StripeRefundDestinationDetailsUSBankTransfer from a JSON string
stripe_refund_destination_details_us_bank_transfer_instance = StripeRefundDestinationDetailsUSBankTransfer.from_json(json)
# print the JSON string representation of the object
print(StripeRefundDestinationDetailsUSBankTransfer.to_json())

# convert the object into a dict
stripe_refund_destination_details_us_bank_transfer_dict = stripe_refund_destination_details_us_bank_transfer_instance.to_dict()
# create an instance of StripeRefundDestinationDetailsUSBankTransfer from a dict
stripe_refund_destination_details_us_bank_transfer_from_dict = StripeRefundDestinationDetailsUSBankTransfer.from_dict(stripe_refund_destination_details_us_bank_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


