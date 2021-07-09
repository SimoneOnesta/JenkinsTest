
# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}


module "ResourceGroupWithvNet" {
  source = "./Modules/ResourceGroup"
  resource_group_name = "pinuzzo"
  location = "westus2"
  address = "10.1.1.0/24"
  vnet_name = "Ciccio"
}



