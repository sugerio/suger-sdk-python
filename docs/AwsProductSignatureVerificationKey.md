# AwsProductSignatureVerificationKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | **str** |  | [optional] 
**public_key_version** | **int** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.aws_product_signature_verification_key import AwsProductSignatureVerificationKey

# TODO update the JSON string below
json = "{}"
# create an instance of AwsProductSignatureVerificationKey from a JSON string
aws_product_signature_verification_key_instance = AwsProductSignatureVerificationKey.from_json(json)
# print the JSON string representation of the object
print(AwsProductSignatureVerificationKey.to_json())

# convert the object into a dict
aws_product_signature_verification_key_dict = aws_product_signature_verification_key_instance.to_dict()
# create an instance of AwsProductSignatureVerificationKey from a dict
aws_product_signature_verification_key_from_dict = AwsProductSignatureVerificationKey.from_dict(aws_product_signature_verification_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


