# AdyenBuyer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **Dict[str, object]** | Settings store key-value pairs such as paymentMethodId,syncWithProvider,providerPaymentMethods. | [optional] 
**shopper_id** | **str** | The shopperId on the adyen platform corresponding to the buyer. | [optional] 

## Example

```python
from suger_sdk_python.models.adyen_buyer import AdyenBuyer

# TODO update the JSON string below
json = "{}"
# create an instance of AdyenBuyer from a JSON string
adyen_buyer_instance = AdyenBuyer.from_json(json)
# print the JSON string representation of the object
print(AdyenBuyer.to_json())

# convert the object into a dict
adyen_buyer_dict = adyen_buyer_instance.to_dict()
# create an instance of AdyenBuyer from a dict
adyen_buyer_from_dict = AdyenBuyer.from_dict(adyen_buyer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


