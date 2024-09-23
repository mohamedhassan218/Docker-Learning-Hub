# Kubernetes (K8s) Deployment Example

## Introduction to Kubernetes (K8s)

Kubernetes, often referred to as K8s, is an open-source platform designed to automate the deployment, scaling, and management of containerized applications. It helps orchestrate containerized applications across a cluster of machines, providing resilience, load balancing, and automation for deployments. With Kubernetes, developers can manage containers at scale in a highly efficient way, handling failover, scaling, and even service discovery.

Kubernetes is widely adopted in cloud-native architectures, making it the backbone of modern infrastructure for microservices and containerized applications.

## Imperative vs Declarative Kubernetes Management

Kubernetes supports two primary methods for managing your cluster and applications: **imperative** and **declarative**. Both methods have their use cases, depending on the situation and preference.

### Imperative
Imperative management involves issuing direct commands to the Kubernetes API to perform actions in real-time. Each command makes immediate changes to the system, and you are responsible for tracking and controlling the state. 

- **Pros**: Quick and easy for small, ad-hoc tasks.
- **Cons**: Difficult to track changes, not easily repeatable, and hard to manage for complex systems.


### Declarative
Declarative management relies on defining the desired state of the system in configuration files (YAML or JSON), and Kubernetes ensures that the current state matches the desired state. This approach is more suited for long-term infrastructure management as it allows better version control and repeatability.

- **Pros**: Better suited for complex applications, easy to track with version control, and allows automation.
- **Cons**: Initial setup can take more time and understanding.


## Nginx Deployment Example

In this lesson, we will deploy an Nginx container using both imperative and declarative methods.

### Imperative Deployment
Use the following command to deploy an Nginx container imperatively:

```bash
kubectl create deployment nginx1 --image=nginx
```

This command directly creates a deployment for the Nginx container.

### Declarative Deployment
First, create a YAML file (`deploy-example.yaml`) with the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx2
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```

Apply the file to create the deployment:

```bash
kubectl create -f deploy-example.yaml
```

### Cleanup
To delete the deployments created in both methods, use the following commands:

```bash
kubectl delete deployment nginx1
kubectl delete deployment nginx2
```
