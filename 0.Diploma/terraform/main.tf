terraform {
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

resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}_RG"
  location = var.location
  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}

resource "azurerm_kubernetes_cluster" "k8s" {
  name                = "${var.prefix}-k8s"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = "${var.prefix}-k8s"
  
  identity {
    type = "SystemAssigned"
  }
  
  linux_profile {
      admin_username = "ubuntu"

      ssh_key {
          key_data = file(var.ssh_public_key)
      }
  }

  default_node_pool {
    name                = "node"
    node_count          = var.node_count
    vm_size             = "Standard_B2s"
  }

  network_profile {
      load_balancer_sku = "Standard"
      network_plugin = "kubenet"
  }

  tags = {
    owner = "Maxim_Cherepennikov@epam.com"
  }
}