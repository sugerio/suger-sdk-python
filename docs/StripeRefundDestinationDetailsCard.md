# StripeRefundDestinationDetailsCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Value of the reference number assigned to the refund. | [optional] 
**reference_status** | **str** | Status of the reference number on the refund. This can be &#x60;pending&#x60;, &#x60;available&#x60; or &#x60;unavailable&#x60;. | [optional] 
**reference_type** | **str** | Type of the reference number assigned to the refund. | [optional] 
**type** | **str** | The type of refund. This can be &#x60;refund&#x60;, &#x60;reversal&#x60;, or &#x60;pending&#x60;. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_refund_destination_details_card import StripeRefundDestinationDetailsCard

# TODO update the JSON string below
json = "{}"
# create an instance of StripeRefundDestinationDetailsCard from a JSON string
stripe_refund_destination_details_card_instance = StripeRefundDestinationDetailsCard.from_json(json)
# print the JSON string representation of the object
print(StripeRefundDestinationDetailsCard.to_json())

# convert the object into a dict
stripe_refund_destination_details_card_dict = stripe_refund_destination_details_card_instance.to_dict()
# create an instance of StripeRefundDestinationDetailsCard from a dict
stripe_refund_destination_details_card_from_dict = StripeRefundDestinationDetailsCard.from_dict(stripe_refund_destination_details_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


