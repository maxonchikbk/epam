terraform plan -var-file="secret.tfvars" -out out.plan
az aks get-credentials --resource-group MaxChe_RG --name MaxChe-k8s