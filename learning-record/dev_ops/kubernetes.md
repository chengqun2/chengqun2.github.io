pod: 包含一个或多个容器（每个pod都有自己的ip地址，pod内的容器共享相同的ip和端口）
deployment(命名空间): 管理pod集群（一次可以启动多个实例）
service: 管理pod中的服务 （通过一个固定的IP来访问各个pod中的服务）


kubernetes（k8s）是什么？pod、service、deployment的关系？
k8s是进行docker容器编排工作。
容器之间的紧密合作出现了pod，希望一次可以起多个实例，就有了deployment多实例管理对象。而有了一组相同的pod之后，我们还需要有一个固定的ip来访问，于是机有了service。


### 将yaml配置文件应用到 Kubernetes 集群中
kubectl apply -f deploy.yml
kubectl get pods
kubectl logs example-6477c68b54-f6kg9
kubectl apply -f service.yml
kubectl get deployments,services,pods
kubectl delete -n default pod/example-6477c68b54-ckl4z
kubectl delete -n default deployment.apps/example
