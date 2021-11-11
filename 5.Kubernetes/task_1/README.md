# Task 1.1
## Install Kubernetes 
```
PS C:\Users\maxon> kubectl config get-contexts
CURRENT   NAME             CLUSTER          AUTHINFO         NAMESPACE
          docker-desktop   docker-desktop   docker-desktop
*         minikube         minikube         minikube         default
PS C:\Users\maxon> kubectl get nodes
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   37m   v1.20.7
PS C:\Users\maxon> kubectl config use-context docker-desktop
Switched to context "docker-desktop".
PS C:\Users\maxon> kubectl get nodes
NAME             STATUS   ROLES                  AGE   VERSION
docker-desktop   Ready    control-plane,master   81d   v1.21.2
```
## Install Kubernetes Dashboard
```
PS C:\Users\maxon> kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.3.1/aio/deploy/recommended.yaml
namespace/kubernetes-dashboard created
serviceaccount/kubernetes-dashboard created
service/kubernetes-dashboard created
secret/kubernetes-dashboard-certs created
secret/kubernetes-dashboard-csrf created
secret/kubernetes-dashboard-key-holder created
configmap/kubernetes-dashboard-settings created
role.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrole.rbac.authorization.k8s.io/kubernetes-dashboard created
rolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
clusterrolebinding.rbac.authorization.k8s.io/kubernetes-dashboard created
deployment.apps/kubernetes-dashboard created
service/dashboard-metrics-scraper created
deployment.apps/dashboard-metrics-scraper created
PS C:\Users\maxon>  kubectl get pod -n kubernetes-dashboard
NAME                                         READY   STATUS    RESTARTS   AGE
dashboard-metrics-scraper-856586f554-qc47w   1/1     Running   0          51s
kubernetes-dashboard-67484c44f6-kzscn        1/1     Running   0          51s
```
## Install Metrics Server
```
PS C:\Users\maxon> kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
serviceaccount/metrics-server created
clusterrole.rbac.authorization.k8s.io/system:aggregated-metrics-reader created
clusterrole.rbac.authorization.k8s.io/system:metrics-server created
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader created
clusterrolebinding.rbac.authorization.k8s.io/metrics-server:system:auth-delegator created
clusterrolebinding.rbac.authorization.k8s.io/system:metrics-server created
service/metrics-server created
deployment.apps/metrics-server created
apiservice.apiregistration.k8s.io/v1beta1.metrics.k8s.io created
```
## Connect to Dashboard
```
PS C:\Users\maxon> kubectl describe sa -n kube-system default
Name:                default
Namespace:           kube-system
Labels:              <none>
Annotations:         <none>
Image pull secrets:  <none>
Mountable secrets:   default-token-d7vpl
Tokens:              default-token-d7vpl
Events:              <none>
PS C:\Users\maxon> kubectl get secrets -n kube-system default-token-d7vpl -o yaml
apiVersion: v1
data:
  ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUM1ekNDQWMrZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJeE1EZ3lNakV3TkRFeE9Wb1hEVE14TURneU1ERXdOREV4T1Zvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTWF2CmFIa09Xb1FFa2E1a1dXeCtwNWVOR1V0SEZXSzhFTTVTdVZSazlsNjZzZmRmb29LSkZrVFhpVmp2UmVMa3pwRmcKcmVlS1ZJNGhDUXZNZm5HL0hFaFUyN1ZBSHdpRG9lNENHKzYzSm1lRjMzSHMxTzRaVEhpaXIrK3l0bDYreld2UApPc09taEhFY1M1ZlFaZzNOZUowQUFyNFEzL3FHQjlSVFh5Z21aUlVxWWVkbHNWbEErY1pxdTBjZVMrZGIwUHdpClgva3BuRDNQL09MYjBEcTZyME1nU0Z6dGFsaGM0YkU0ZU1yclNJcUNQMUpHWWlTVG9NYjVoZWo2WUt4YnJuM2wKRHFZOHNuQk92bkNCR1p2YlhoWHBsVjgzaTVDYzlBREhIb0xsWndBa1F5NThhdmZJUm8zZXpHM3djQkVUSC82awpaVWs2MVRCVkFvVk9GdGtYVzUwQ0F3RUFBYU5DTUVBd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZKY1l1eDRtWnhyeHo3cU5QTXRXZ0NCY00zSHNNQTBHQ1NxR1NJYjMKRFFFQkN3VUFBNElCQVFDZmZxSXlocGVZVkN2M2NseTlZdlp1MjZaSE9hSWJCM3ROYitHcFJRd3dUbTlhSGVKSQo5RUlLbExkTFF3VFVpZlNoeGZqUHJCWkFuclV3S0p1YWpWdVY2QnZ0Y1g0ZTNBKzduckpOK0ZZVlo3WnhsajAvCjBEa25wTmplSTBXQ2pLbFkyallmOUgvLzcrRWJTbk9nYkJPWnNFRVhqZGQ5QURkck9PT3dXdU5rOEc0akR6Y2UKYkNSaUd5ZVYyOUVRa1k2ZXBQN09qaGE3YmE0bGZYc09Sb0NHRFMvYURpZEMwMFNEOTMzTkxkd2swMkhpTElYbgpRNS8zUHpEQkFZTDlFUEhUUjB4V2xWUUxjZGtlcXl0amcxSnJpZEZBYzRXWXprUGpybG5FRkU2MEg5Q0hlWnRZCjQwSEZ0V2ZOOUt3N20zd2Zxc0wxQzBxR1lraUkxby9jK3hwWQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
  namespace: a3ViZS1zeXN0ZW0=
  token: ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklsTjZiR2xJZDI5MVNVWTNSbU54VVVNeldtTTJYMmRLYjJOamJWODVkbGhwY1ROVFFWY3haRlo2WjFFaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUpyZFdKbExYTjVjM1JsYlNJc0ltdDFZbVZ5Ym1WMFpYTXVhVzh2YzJWeWRtbGpaV0ZqWTI5MWJuUXZjMlZqY21WMExtNWhiV1VpT2lKa1pXWmhkV3gwTFhSdmEyVnVMV1EzZG5Cc0lpd2lhM1ZpWlhKdVpYUmxjeTVwYnk5elpYSjJhV05sWVdOamIzVnVkQzl6WlhKMmFXTmxMV0ZqWTI5MWJuUXVibUZ0WlNJNkltUmxabUYxYkhRaUxDSnJkV0psY201bGRHVnpMbWx2TDNObGNuWnBZMlZoWTJOdmRXNTBMM05sY25acFkyVXRZV05qYjNWdWRDNTFhV1FpT2lJMk5EQmhNamd5TnkwNVptRTNMVFE1T0RRdFltSmxaQzB4TURsbE5tRXhOemRqTURRaUxDSnpkV0lpT2lKemVYTjBaVzA2YzJWeWRtbGpaV0ZqWTI5MWJuUTZhM1ZpWlMxemVYTjBaVzA2WkdWbVlYVnNkQ0o5LnJuakI4TDVIMlp3dW5vcEQ0STFfejlfZGZpTVFqWnBEWjJVTF9WUk95MkZhckxJemhnYlF6ZGZVa05adGRpVHJ0WWVyU3h3STd2N0RXZVJqUXktZUExb2h4WXhOSWxzS1J5N1daRGotSHRTY1dkczd3b0d1WmlSZ3lWZVpvcTgtY1NXRUM4ZnlPUm1ZbEtFQ3RBLU92b3ZaYnhpck9WNHZyZV9OcV9IVU1TZ0gzRHNZSlBVZXdNaF9PMjhnSVJiZk5KRmtmT2FYdVpTTFhYcXZoWDdOdW1yblpjMVNEMWc3cl9XQnp5Mm11NlpCR3lWVXM0RGtfekszRkZOWGxTa1NKako4NlNJQTczbGVUZGpzc3ZubF90OGF4NDRINWtVbkd1Zm42RVJwZGdvcWNhRk9fcXl1VzJKME1NM21saElWemRscDNwd1NEN180RjN4WU52d2tmdw==
kind: Secret
metadata:
  annotations:
    kubernetes.io/service-account.name: default
    kubernetes.io/service-account.uid: 640a2827-9fa7-4984-bbed-109e6a177c04
  creationTimestamp: "2021-08-22T10:42:02Z"
  name: default-token-d7vpl
  namespace: kube-system
  resourceVersion: "387"
  uid: 16815c2c-0012-4c9c-b781-ff4026d22c6f
type: kubernetes.io/service-account-token
```
# Task 1.2
```
PS C:\Users\maxon> k create deployment nginx --image nginx --replicas 2
deployment.apps/nginx created
PS C:\Users\maxon> k get deployments
NAME    READY   UP-TO-DATE   AVAILABLE   AGE
nginx   2/2     2            2           16s
PS C:\Users\maxon> k get pods
NAME                     READY   STATUS    RESTARTS   AGE
nginx-6799fc88d8-th7tm   1/1     Running   0          23s
nginx-6799fc88d8-zc7vl   1/1     Running   0          23s
PS C:\Users\maxon> k delete pod nginx-6799fc88d8-th7tm
pod "nginx-6799fc88d8-th7tm" deleted
PS C:\Users\maxon> k get pods
NAME                     READY   STATUS    RESTARTS   AGE
nginx-6799fc88d8-8rvnc   1/1     Running   0          22s
nginx-6799fc88d8-zc7vl   1/1     Running   0          57s
```
# Task 1.1
Requirements:
- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
## Verify kubectl installation
```bash
kubectl version --client
```
Output, that indicates that everything is working.
```bash
Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.0", GitCommit:"9e991415386e4cf155a24b1da15becaa390438d8", GitTreeState:"clean", BuildDate:"2020-03-25T14:58:59Z", GoVersion:"go1.13.8", Compiler:"gc", Platform:"windows/amd64"}
```

## Setup autocomplete for kubectl
```bash
source <(kubectl completion bash) 
```

```bash
minikube start --driver=virtualbox
```
## Get information about cluster
```bash
$ kubectl cluster-info
```
Sample output, that indicates that everything is working.
```bash
Kubernetes master is running at https://192.168.99.107:8443
CoreDNS is running at https://192.168.99.107:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'
```
## get information about available nodes
```bash
$ kubectl get nodes
```
Sample output, that indicates that everything is working.
```bash
NAME       STATUS   ROLES                  AGE     VERSION
minikube   Ready    control-plane,master   9m52s   v1.22.2
```

# Install [Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)
```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.3.1/aio/deploy/recommended.yaml
```
# Check kubernetes-dashboard ns
```bash
 kubectl get pod -n kubernetes-dashboard
```
Sample output
```bash
NAME                                         READY   STATUS    RESTARTS   AGE
dashboard-metrics-scraper-5594697f48-ng9x6   1/1     Running   0          30m
kubernetes-dashboard-57c9bfc8c8-qjt2s        1/1     Running   0          30m
```
# Install [Metrics Server](https://github.com/kubernetes-sigs/metrics-server#deployment)
```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Update deployment
```bash
kubectl edit -n kube-system deployment metrics-server
```
```bash
spec:
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=443
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-insecure-tls
        - --kubelet-use-node-status-port
```

# Connect to Dashboard
## Get token
### Manual

```bash
kubectl describe sa -n kube-system default
# copy token name
kubectl get secrets -n kube-system
kubectl get secrets -n kube-system token_name_from_first_command -o yaml
echo -n "token_from_previous_step" | base64 -d
```
# Same thing in one command
```bash
 kubectl get secrets -n kube-system $(kubectl describe sa -n kube-system default|grep Tokens|awk '{print $2}') -o yaml|grep -E "^[[:space:]]*token:"|awk '{print $2}'|base64 -d
```

### Auto
```bash
export SECRET_NAME=$(kubectl get sa -n kube-system default -o jsonpath='{.secrets[0].name}')
export TOKEN=$(kubectl get secrets -n kube-system $SECRET_NAME -o jsonpath='{.data.token}' | base64 -d)
echo $TOKEN
```

## Connect to Dashboard
```bash
kubectl proxy
```
In browser connect to http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

# Task 1.2
# Kubernetes resources introduction
```bash
kubectl run web --image=nginx:latest
```
- take a look at created resource in cmd "kubectl get pods"
- take a look at created resource in Dashboard
- take a look at created resource in cmd
```bash
minikube ssh
docker container ls
```

## [Specification](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/)
```bash
kubectl explain pods.spec
```
Apply manifests (download from repository)
```bash
kubectl apply -f pod.yaml
kubectl apply -f rs.yaml
```
Look at pod
```bash
kubectl get pod
```
# You can create simple manifest from cmd
```bash
kubectl run web --image=nginx:latest --dry-run=client -o yaml
```
### Homework
* Create a deployment nginx. Set up two replicas. Remove one of the pods, see what happens.
