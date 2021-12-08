output "kube_config" {
  value     = azurerm_kubernetes_cluster.k8s.kube_config_raw
  sensitive = true
}

output "login_server" {
  value = data.azurerm_container_registry.acr.login_server
}

output "admin_username" {
  value = data.azurerm_container_registry.acr.admin_username
}

output "admin_password" {
  value = data.azurerm_container_registry.acr.admin_password
}