FLASK - MYSQL CRUD DEPLOYMENT ON A MINIKUBE CLUSTER.

My repo is a tutorial on deploying a Flask ap which reads and writes to a MYSQL Database. 

I have 2 subfolder for each of the deployment - named appropriately. 


Listed below are the 2 deployments as per the folders uploaded, and their contents. 

- flask_deployment
	- deployment.yaml
	- service.yaml

- mysql_deployment
	- deployment.yaml
	- service.yaml
	- pv.yaml (Encompasses the PersistantVolume and PersistantVolumeClaim objects)


To run the mysql app, the yaml files should be run in the order: 1)pv.yaml 2)service.yaml 3)deployment.yaml - run using kubectl create -f . 
I specify this order so the deployment can already see the pv and pvc created, and not complain that it cant find any volumes. 

To run the flask app, I run the deployment.yaml and service.yaml command. 
To expose the flask out of the cluster, the command "minikube service <<service_name>>" which In this case, I substitute 
"server-service" - which is my service name. 
With the above, the output is a URL which can be used to access the flask app on the host. 

Not included in this repo: 
To access the app publically, I use nginx as my entrypoint, which points to the minikube service URL. 




