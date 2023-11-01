# AwsAceIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**AwsIntegrationCredential**](AwsIntegrationCredential.md) |  | [optional] 
**enable_assume_iam_role** | **bool** | Enable assume IAM role to access the client&#39;s AWS ACE S3 bucket. If false, Suger will use the AwsIntegrationCredential to access the client&#39;s AWS ACE S3 bucket. | [optional] 
**iam_role_arn** | **str** | The AWS IAM role for Suger service to assume to access the client&#39;s AWS ACE S3 bucket. Applicable only if EnableAssumeIamRole is true. | [optional] 
**partner_id** | **str** | The partner ID of the ISV/Seller in AWS Partner Network. | [optional] 
**paused** | **bool** | Is the integration paused. | [optional] 
**s3_bucket_name** | **str** | The Name of the S3 bucket for AWS APN Customer Engagement Program (ACE) to sync the leads &amp; opportunities. | [optional] 
**s3_bucket_region** | **str** | The region of the S3 bucket for AWS APN Customer Engagement Program (ACE) to sync the leads &amp; opportunities. | [optional] 
**secret_key** | **str** | The secret key used to store the AwsIntegrationCredential in AWS Secret manager. for internal usage only. | [optional] 

## Example

```python
from openapi_client.models.aws_ace_integration import AwsAceIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAceIntegration from a JSON string
aws_ace_integration_instance = AwsAceIntegration.from_json(json)
# print the JSON string representation of the object
print AwsAceIntegration.to_json()

# convert the object into a dict
aws_ace_integration_dict = aws_ace_integration_instance.to_dict()
# create an instance of AwsAceIntegration from a dict
aws_ace_integration_form_dict = aws_ace_integration.from_dict(aws_ace_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


