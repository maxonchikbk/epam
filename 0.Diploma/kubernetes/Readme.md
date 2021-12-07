terraform apply -var-file="secret.tfvars"
az aks get-credentials --resource-group MaxChe_RG --name MaxChe-k8s
kubectl create secret docker-registry regcred --docker-server=maxchecr.azurecr.io --docker-username=MaxCheCR --docker-password=R+YxlIz6K7lG=kdQWp0K1iCLkM+hR9qM