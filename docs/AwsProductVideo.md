# AwsProductVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_video import AwsProductVideo

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductVideo from a JSON string
aws_product_video_instance = AwsProductVideo.from_json(json)
# print the JSON string representation of the object
print(AwsProductVideo.to_json())

# convert the object into a dict
aws_product_video_dict = aws_product_video_instance.to_dict()
# create an instance of AwsProductVideo from a dict
aws_product_video_from_dict = AwsProductVideo.from_dict(aws_product_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


