terraform apply -var-file="secret.tfvars"
az aks get-credentials --resource-group MaxChe_RG --name MaxChe-k8s
kubectl create secret docker-registry regcred --dry-run=client -oyaml --docker-server=maxchecr.azurecr.io --docker-username=MaxCheCR --docker-password=mThBAVGcN7uDAuGx86R6Sk8/SVwBEEC8