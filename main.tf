provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example"
  location = "West Europe"
}

module "module_source_policy_demo" {
  source  = "Azure/vnet/azurerm"
  version = "4.1.0"

  resource_group_name = "example"
  use_for_each        = true
  vnet_location       = "West Europe"
}
