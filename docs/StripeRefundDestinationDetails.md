# StripeRefundDestinationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**StripeRefundDestinationDetailsCard**](StripeRefundDestinationDetailsCard.md) |  | [optional] 
**type** | **str** | The type of transaction-specific details of the payment method used in the refund (e.g., &#x60;card&#x60;). An additional hash is included on &#x60;destination_details&#x60; with a name matching this value. It contains information specific to the refund transaction. | [optional] 
**us_bank_transfer** | [**StripeRefundDestinationDetailsUSBankTransfer**](StripeRefundDestinationDetailsUSBankTransfer.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_refund_destination_details import StripeRefundDestinationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StripeRefundDestinationDetails from a JSON string
stripe_refund_destination_details_instance = StripeRefundDestinationDetails.from_json(json)
# print the JSON string representation of the object
print(StripeRefundDestinationDetails.to_json())

# convert the object into a dict
stripe_refund_destination_details_dict = stripe_refund_destination_details_instance.to_dict()
# create an instance of StripeRefundDestinationDetails from a dict
stripe_refund_destination_details_from_dict = StripeRefundDestinationDetails.from_dict(stripe_refund_destination_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


