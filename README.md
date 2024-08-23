# Works with dir scan
```
$ checkov --quiet --skip-check CKV_TF_1 -d . --external-checks-dir policy/
2024-08-23 18:06:32,279 [ThreadPoolEx] [WARNI]  Failed to download module Azure/vnet/azurerm:4.1.0 (for external modules, the --download-external-modules flag is required)
terraform scan results:

Passed checks: 1, Failed checks: 1, Skipped checks: 0

Check: FOO: "I will never run with a tfplan :("
	FAILED for resource: module_source_policy_demo
	File: /main.tf:10-17

		10 | module "module_source_policy_demo" {
		11 |   source  = "Azure/vnet/azurerm"
		12 |   version = "4.1.0"
		13 | 
		14 |   resource_group_name = "example"
		15 |   use_for_each        = true
		16 |   vnet_location       = "West Europe"
		17 | }

```

# Doesnt work with tfplan
```
checkov --quiet --skip-check CKV_TF_1 -f tfplan --external-checks-dir policy/

# no further output
```
