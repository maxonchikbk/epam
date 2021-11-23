docker build -t maxonchik/react_app .\react\
docker push maxonchik/react_app
kubectl rollout restart -f .\react\react-deployment.yaml
pause
kubectl get po  