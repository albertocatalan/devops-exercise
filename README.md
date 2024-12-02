# Abraxas DevOps Exercise: Flask App with CI/CD, Kubernetes, and Persistent State

## Requirements to Run the Application

Before running the application, make sure the following tools are set up in your environment:

### Required Tools

- **Git**: To clone the repository and manage the source code.
  - [Download Git](https://git-scm.com/)

- **Docker**: To run the container image.
  - [Install Docker](https://www.docker.com/get-started)

- **Minikube**: To create and manage a local Kubernetes cluster.
  - [Install Minikube](https://minikube.sigs.k8s.io/docs/)

- **Kubernetes**: To orchestrate the containers and deploy the application.
  - [Install Kubernetes](https://kubernetes.io/docs/setup/)

- **Kubectl**: Command-line tool to interact with the Kubernetes cluster.
  - [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)

- **Docker Hub Account**: To store and access the container images.
  - [Create Docker Hub Account](https://hub.docker.com/)

- **GitHub Account**: To access the project repository.
  - [Create GitHub Account](https://github.com/)

---

## Steps to Run the Application

1. **Clone the Repository**

   Clone the repository from GitHub:

   ```bash
   git clone https://github.com/albertocatalan/devops-exercise.git
   ```

   Or use SSH if preferred:

   ```bash
   git clone git@github.com:albertocatalan/devops-exercise.git
   ```

2. **Deploy the Application to Kubernetes**

   Make sure Minikube is running:

   ```bash
   minikube start
   ```

   Apply the Kubernetes configuration files to deploy the Flask app:

   ```bash
   kubectl apply -f deployment.yml
   kubectl apply -f service.yml
   ```

3. **Access the Application via Minikube**

   Once the service is deployed, use the following command to get the service URL and access the Flask app:

   ```bash
   minikube service flask-app-service --url
   ```

   This command will return the URL to access the application running inside Minikube.

4. **Check Application Logs**

   To check the logs of the pods to ensure everything is running smoothly, use:

   ```bash
   kubectl get pods
   kubectl logs <pod-name>
   ```

---

## Docker Hub Image

The Flask application is already containerized and stored on Docker Hub. You can pull the image directly from the following repository:

```bash
docker pull albertocatalan/flask-app
```

---

## Kubernetes Deployment

The Kubernetes deployment is defined in the `deployment.yml` and `service.yml` files. These files specify the number of replicas, persistent storage for the SQLite database, and the service setup to expose the application to external traffic.

To deploy, simply apply the Kubernetes configuration files as shown above.

---

## Technologies Used

- **Flask**: A lightweight Python web framework.
- **Docker**: For containerizing the application.
- **GitHub Actions**: For CI/CD automation.
- **Kubernetes**: For deployment, scaling, and managing the app.
- **SQLite**: For storing the POST request counter persistently.
- **Minikube**: To simulate a local Kubernetes environment for testing and development.

---
## Method
For this DevOps exercise, I started by setting up the necessary tools and environment. This included forking the repository, cloning it locally, and ensuring I had a GitHub account, Docker Hub credentials, and access to a Kubernetes cluster. Minikube was also used to simulate a local Kubernetes cluster for testing and deployment.

## Step 1: Dockerize the Service

I began by creating a `Dockerfile` to containerize the Flask app. This was essential because Docker helps ensure that the application runs consistently across environments, whether in development or production. I used a lightweight `python:3.9-slim` image to minimize the image size and increase efficiency. In the `Dockerfile`, I copied the application code and dependencies into the image and installed the required packages via pip.

## Step 2: Implementing CI/CD with GitHub Actions

I set up a CI/CD pipeline using GitHub Actions. The goal here was to automate the build and deployment of the Docker image. In the `.github/workflows/docker-flask-app-pipeline.yml` file, I defined the workflow to trigger whenever changes were pushed to the `master` branch.

- First, the pipeline checks out the code to ensure the latest version is used for building the Docker image.
- Then, it logs into Docker Hub using secure credentials stored in GitHub secrets.
- After that, it builds the Docker image using the `docker build` command, tagging it with the `latest` tag for easy access.
- Finally, the pipeline pushes the built image to Docker Hub, making it accessible for future deployments and scaling.

## Step 3: Kubernetes Deployment

For deployment, I created a Kubernetes configuration file, `deployment.yml`, to deploy the Flask app on the Kubernetes cluster. The configuration includes:

- **Deployment**: I set the application to run with 3 replicas to ensure scalability and availability. I also defined a persistent volume to store the SQLite database, which ensures the POST request counter remains consistent even when pods are restarted or scaled.
- **Service**: I created a service to expose the Flask app to the outside world, allowing traffic to reach the application. This setup uses a load balancer to distribute traffic evenly across the pods, ensuring the application scales effectively.

## Step 4: Extra Points Flask Application Enhancements (Extra: Shared POST Count Across Pods)

To meet the requirement of maintaining a counter of POST requests, I modified the `app.py` file. Initially, I stored the counter in memory, but since we need the counter to be shared across replicas, I switched to using SQLite with a persistent volume. This approach ensures that the counter value is stored persistently and is accessible to all pods, even after restarts.

In the updated `app.py`, I created functions to initialize and interact with the SQLite database to store and update the counter:
- The **GET route** now returns the current POST request count, making it easy to monitor.
- The **POST route** increments the counter each time a new POST request is made.

This ensures that the counter remains consistent across all replicas and can be easily tracked.

## Step 5 Pull Request Workflow

As part of fostering a DevOps culture and ensuring best practices in deployment, monitoring, and scaling applications, I implemented a pull request workflow in the repository. 

I created a new branch named `test`, enabling interaction limits for external users as follows:

- Restricted interactions to contributors and collaborators who had previously committed to the repository.  
- Configured the branch to enforce a "cool-down" period during discussions or when unwanted interactions might arise.  

This setup ensures a collaborative and secure environment for future contributions, while maintaining a streamlined review process. Additionally, the workflow supports the principles of continuous integration, encouraging team alignment and code quality.  

By merging a commit from the `devops-files` branch into `master`, I demonstrated how pull requests promote better collaboration and adherence to DevOps principles in practice.

## Final Step: Testing and Scaling

Once everything was set up, I deployed the application to the Kubernetes cluster. To verify it was working as expected, I accessed the service using `minikube service flask-app-service` to see the Flask app in action. By scaling the number of replicas, I ensured the app could handle multiple requests while maintaining the shared counter value.

This setup ensures we followed the DevOps principles of automating deployments, monitoring, scaling, and maintaining consistent application behavior across environments. Each decision was made with scalability and reliability in mind, promoting a culture of continuous integration and deployment.

## Notes

- The app uses a shared POST request counter stored in an SQLite database that persists across pod restarts by leveraging persistent volumes in Kubernetes.


## Author

This project was developed by [Alberto Catalán]

- GitHub (Project Repository): [albertocatalan](https://github.com/albertocatalan)
- GitHub (Personal Projects): [cataluniat](https://github.com/cataluniat)
- LinkedIn: [Alberto Catalán](https://mx.linkedin.com/in/alberto-catalan)
- Email: [businesscatalangmail.com](mailto:businesscatalangmail.com)
- Position: Solutions Architect Associate (Certified)

This exercise is intended solely for the objectives defined by Grupo Abraxas.
