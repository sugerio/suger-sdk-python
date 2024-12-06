# UpdateProductParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_url** | **str** |  | 
**id** | **str** |  | 
**organization_id** | **str** |  | 

## Example

```python
from suger_sdk_python.models.update_product_params import UpdateProductParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductParams from a JSON string
update_product_params_instance = UpdateProductParams.from_json(json)
# print the JSON string representation of the object
print(UpdateProductParams.to_json())

# convert the object into a dict
update_product_params_dict = update_product_params_instance.to_dict()
# create an instance of UpdateProductParams from a dict
update_product_params_from_dict = UpdateProductParams.from_dict(update_product_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


