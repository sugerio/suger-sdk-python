# AzureProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilities** | [**List[AzureProductAvailability]**](AzureProductAvailability.md) |  | [optional] 
**branches** | [**List[AzureProductBranch]**](AzureProductBranch.md) |  | [optional] 
**external_ids** | [**List[AzureTypeValue]**](AzureTypeValue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**is_modular_publishing** | **bool** |  | [optional] 
**listings** | [**List[AzureProductListing]**](AzureProductListing.md) |  | [optional] 
**name** | **str** |  | [optional] 
**package_configurations** | [**List[AzureProductPackageConfiguration]**](AzureProductPackageConfiguration.md) |  | [optional] 
**plans** | [**List[AzureMarketplacePriceAndAvailabilityPrivateOfferPlan]**](AzureMarketplacePriceAndAvailabilityPrivateOfferPlan.md) | All plans under this product | [optional] 
**properties** | [**List[AzureProductProperty]**](AzureProductProperty.md) |  | [optional] 
**resource_type** | **str** |  | [optional] 
**setup** | [**AzureProductSetup**](AzureProductSetup.md) |  | [optional] 
**submissions** | [**List[AzureProductSubmission]**](AzureProductSubmission.md) |  | [optional] 
**variants** | [**List[AzureProductVariant]**](AzureProductVariant.md) |  | [optional] 

## Example

```python
from openapi_client.models.azure_product import AzureProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AzureProduct from a JSON string
azure_product_instance = AzureProduct.from_json(json)
# print the JSON string representation of the object
print AzureProduct.to_json()

# convert the object into a dict
azure_product_dict = azure_product_instance.to_dict()
# create an instance of AzureProduct from a dict
azure_product_form_dict = azure_product.from_dict(azure_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


