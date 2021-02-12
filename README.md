# containerized-datascience

## Awesome presentation

https://docs.google.com/presentation/d/1pDzvSciCwmjYjrjwYZ-ayMIijoipMVRH2Ub5u5ZhSrM/edit?usp=sharing

## Run locally

```
docker build -t data-science . 
docker run data-science
```

## Start minikube

```
minikube start
minikube dashboard

minikube docker-env
eval $(minikube -p minikube docker-env)
docker build -t data-science:v0 .
```


## Let it run once
```
kubectl run data-science --rm -i --tty --restart=Never --image=data-science:v1 
```


## A server-like start (aka: deployment)
```
kubectl run data-science --image data-science:v0
kubectl delete -n default deployment data-science
```