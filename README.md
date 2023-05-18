Cloud Native Application Architecture Nanodegree 

TechTrends Project


TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them. We package and deploy TechTrends to Kubernetes using a CI/CD pipeline.


The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

Web Application & Database

Python
Flask
SQLite

CI/CD tools

Containerization & Virtualization
Docker
Vagrant

Automating Deployment & management of containerized applications
k3s

CI stages tooling
Github Actions

CD tooling
argo-cd

Deployment on multiple Kubernetes clusters
Helm


Project Steps Overview

Apply the best development practices and develop the status and health check endpoints for the TechTrends application.
Package the TechTrends application by creating a Dockerfile and Docker image.
Implement the Continuous Integration practices, by using GitHub Actions to automate the build and push of the Docker image to DockerHub.
Construct the Kubernetes declarative manifests to deploy TechTrends to a sandbox namespace within a Kubernetes cluster. The cluster should be provisioned using k3s in a vagrant box.
Template the Kubernetes manifests using a Helm chart and provide the input configuration files for staging and production environments.
Implement the Continuous Delivery practices, by deploying the TechTrends application to staging and production environments using ArgoCD and the Helm chart.


