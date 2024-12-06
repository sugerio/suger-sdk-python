# StripeProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Whether the product is currently available for purchase. | [optional] 
**created** | **int** | Time at which the object was created. Measured in seconds since the Unix epoch. | [optional] 
**description** | **str** | The product&#39;s description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes. | [optional] 
**id** | **str** | Unique identifier for the product in Stripe. | [optional] 
**images** | **List[str]** | A list of up to 8 URLs of images for this product, meant to be displayable to the customer. | [optional] 
**livemode** | **bool** | Has the value &#x60;true&#x60; if the object exists in live mode or the value &#x60;false&#x60; if the object exists in test mode. | [optional] 
**marketing_features** | [**List[StripeProductMarketingFeature]**](StripeProductMarketingFeature.md) | A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table). | [optional] 
**metadata** | **Dict[str, str]** | Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. | [optional] 
**name** | **str** | The product&#39;s name, meant to be displayable to the customer. | [optional] 
**object** | **str** | String representing the object&#39;s type. Always has the value &#x60;product&#x60;. | [optional] 
**package_dimensions** | [**StripeProductPackageDimensions**](StripeProductPackageDimensions.md) | The dimensions of this product for shipping purposes. | [optional] 
**shippable** | **bool** | Whether this product is shipped (i.e., physical goods). | [optional] 
**statement_descriptor** | **str** | Extra information about a product which will appear on your customer&#39;s credit card statement. In the case that multiple products are billed at once, the first statement descriptor will be used. | [optional] 
**tax_code** | **object** | A [tax code](https://stripe.com/docs/tax/tax-categories) ID. | [optional] 
**unit_label** | **str** | A label that represents units of this product. When set, this will be included in customers&#39; receipts, invoices, Checkout, and the customer portal. | [optional] 
**updated** | **int** | Time at which the product was last updated. Measured in seconds since the Unix epoch. | [optional] 
**url** | **str** | A URL of a publicly-accessible webpage for this product. | [optional] 

## Example

```python
from suger_sdk_python.models.stripe_product import StripeProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StripeProduct from a JSON string
stripe_product_instance = StripeProduct.from_json(json)
# print the JSON string representation of the object
print(StripeProduct.to_json())

# convert the object into a dict
stripe_product_dict = stripe_product_instance.to_dict()
# create an instance of StripeProduct from a dict
stripe_product_from_dict = StripeProduct.from_dict(stripe_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


