# StripePaymentMethodCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | Card brand. | [optional] 
**country** | **str** | Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you&#39;ve collected. | [optional] 
**display_brand** | **str** | The brand to use when displaying the card, this accounts for customer&#39;s brand choice on dual-branded cards. Can be &#x60;american_express&#x60;, &#x60;cartes_bancaires&#x60;, &#x60;diners_club&#x60;, &#x60;discover&#x60;, &#x60;eftpos_australia&#x60;, &#x60;interac&#x60;, &#x60;jcb&#x60;, &#x60;mastercard&#x60;, &#x60;union_pay&#x60;, &#x60;visa&#x60;, or &#x60;other&#x60; and may contain more values in the future. | [optional] 
**exp_month** | **int** | Two-digit number representing the card&#39;s expiration month. | [optional] 
**exp_year** | **int** | Four-digit number representing the card&#39;s expiration year. | [optional] 
**fingerprint** | **str** | Uniquely identifies this particular card number. You can use this attribute to check whether two customers who’ve signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number. | [optional] 
**funding** | **str** | Card funding type. Can be &#x60;credit&#x60;, &#x60;debit&#x60;, &#x60;prepaid&#x60;, or &#x60;unknown&#x60;. | [optional] 
**last4** | **str** | The last four digits of the card. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_payment_method_card import StripePaymentMethodCard

# TODO update the JSON string below
json = "{}"
# create an instance of StripePaymentMethodCard from a JSON string
stripe_payment_method_card_instance = StripePaymentMethodCard.from_json(json)
# print the JSON string representation of the object
print(StripePaymentMethodCard.to_json())

# convert the object into a dict
stripe_payment_method_card_dict = stripe_payment_method_card_instance.to_dict()
# create an instance of StripePaymentMethodCard from a dict
stripe_payment_method_card_from_dict = StripePaymentMethodCard.from_dict(stripe_payment_method_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


