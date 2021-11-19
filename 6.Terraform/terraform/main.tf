terraform {

  required_version = ">=0.12"
  
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "~>2.0"
    }
  }
}

provider "azurerm" {
  features {}
}

## <https://www.terraform.io/docs/providers/azurerm/r/resource_group.html>
resource "azurerm_resource_group" "mc" {
  name     = "${var.prefix}_RG"
  location = var.location
  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}

resource "azurerm_virtual_network" "mc" {
  name                = "${var.prefix}-network"
  location            = azurerm_resource_group.mc.location
  resource_group_name = azurerm_resource_group.mc.name
  address_space       = ["10.1.0.0/16"]
  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}

resource "azurerm_subnet" "mc" {
  name                 = "${var.prefix}-subnet"
  virtual_network_name = azurerm_virtual_network.mc.name
  resource_group_name  = azurerm_resource_group.mc.name
  address_prefixes     = ["10.1.0.0/22"]
  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}

resource "azurerm_kubernetes_cluster" "mc" {
  name                = "${var.prefix}-k8s"
  location            = azurerm_resource_group.mc.location
  resource_group_name = azurerm_resource_group.mc.name
  dns_prefix          = "${var.prefix}-k8s"

  default_node_pool {
    name                = "default"
    node_count          = 3
    vm_size             = "Standard_D2_v2"
    type                = "VirtualMachineScaleSets"
    availability_zones  = ["1", "2", "3"]
    enable_auto_scaling = true
    min_count           = 2
    max_count           = 4

    # Required for advanced networking
    vnet_subnet_id = azurerm_subnet.mc.id
  }

  identity {
    type = "SystemAssigned"
  }

  # role_based_access_control {
  #   azure_active_directory {
  #     client_app_id     = var.client_app_id
  #     server_app_id     = var.server_app_id
  #     server_app_secret = var.server_app_secret
  #     tenant_id         = var.tenant_id
  #   }
  #   enabled = true
  # }

  network_profile {
    network_plugin    = "azure"
    load_balancer_sku = "standard"
    network_policy    = "calico"
  }

  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}