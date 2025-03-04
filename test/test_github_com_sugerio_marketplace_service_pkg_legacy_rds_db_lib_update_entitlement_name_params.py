# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from suger_sdk_python.models.github_com_sugerio_marketplace_service_pkg_legacy_rds_db_lib_update_entitlement_name_params import GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams

class TestGithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams(unittest.TestCase):
    """GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams:
        """Test GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams`
        """
        model = GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams()
        if include_optional:
            return GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams(
                id = '',
                name = '',
                organization_id = ''
            )
        else:
            return GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams(
        )
        """

    def testGithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams(self):
        """Test GithubComSugerioMarketplaceServicePkgLegacyRdsDbLibUpdateEntitlementNameParams"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
