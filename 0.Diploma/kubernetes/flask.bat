docker build -t maxonchik/flask_app .\flask\
docker push maxonchik/flask_app
kubectl rollout restart -f .\flask\flask-deployment.yaml
pause
kubectl get po  