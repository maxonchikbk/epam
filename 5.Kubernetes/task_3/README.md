1. We published minio "outside" using nodePort. Do the same but using ingress.
* ### [ingress.yaml](https://github.com/maxonchikbk/epam/blob/main/5.Kubernetes/task_3/ingress.yaml)
___
2. Publish minio via ingress so that minio by ip_minikube and nginx returning hostname (previous job) by path ip_minikube/web are available at the same time.
* ### [deployment.yaml](https://github.com/maxonchikbk/epam/blob/main/5.Kubernetes/task_3/deployment.yaml) :
```
        - image: nginx:latest
          name: nginx
          ports:
          - containerPort: 80
          volumeMounts:
            - name: config-nginx
              mountPath: /etc/nginx/conf.d
```              
* ### [ingress.yaml](https://github.com/maxonchikbk/epam/blob/main/5.Kubernetes/task_3/ingress.yaml) :

```
      - path: /
        pathType: Prefix
        backend:
          service:
             name: minio
             port: 
                number: 9001
      - path: /web
        pathType: Prefix
        backend:
          service:
             name: minio-web
             port: 
                number: 80
```
* ### [services.yaml](https://github.com/maxonchikbk/epam/blob/main/5.Kubernetes/task_3/services.yaml)
___
3. Create deploy with emptyDir save data to mountPoint emptyDir, delete pods, check data.
Emptydir doesn't keep data after deleting a pod. PersistentVolume do.
```
      volumeMounts:
          - name: data
              mountPath: "/data"              
          - name: empty
              mountPath: "/empty" 
      volumes:      
        - name: data
          persistentVolumeClaim:
            claimName: minio-deployment-claim
        - name: empty
          emptyDir: {}        
```
# Task 3
### [Read more about CSI](https://habr.com/ru/company/flant/blog/424211/)
### Create pv in kubernetes
```bash
kubectl apply -f pv.yaml
```
### Check our pv
```bash
kubectl get pv
```
### Sample output
```bash
NAME                  CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM   STORAGECLASS   REASON   AGE
minio-deployment-pv   5Gi        RWO            Retain           Available                                   5s
```
### Create pvc
```bash
kubectl apply -f pvc.yaml
```
### Check our output in pv 
```bash
kubectl get pv
NAME                  CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                            STORAGECLASS   REASON   AGE
minio-deployment-pv   5Gi        RWO            Retain           Bound    default/minio-deployment-claim                           94s
```
Output is change. PV get status bound.
### Check pvc
```bash
kubectl get pvc
NAME                     STATUS   VOLUME                CAPACITY   ACCESS MODES   STORAGECLASS   AGE
minio-deployment-claim   Bound    minio-deployment-pv   5Gi        RWO                           79s
```
### Apply deployment minio
```bash
kubectl apply -f deployment.yaml
```
### Apply svc nodeport
```bash
kubectl apply -f minio-nodeport.yaml
```
Open minikup_ip:node_port in you browser
### Apply statefulset
```bash
kubectl apply -f statefulset.yaml
```
### Check pod and statefulset
```bash
kubectl get pod
kubectl get sts
```

### Homework
* We published minio "outside" using nodePort. Do the same but using ingress.
* Publish minio via ingress so that minio by ip_minikube and nginx returning hostname (previous job) by path ip_minikube/web are available at the same time.
* Create deploy with emptyDir save data to mountPoint emptyDir, delete pods, check data.
* Optional. Raise an nfs share on a remote machine. Create a pv using this share, create a pvc for it, create a deployment. Save data to the share, delete the deployment, delete the pv/pvc, check that the data is safe.