# Document Portal: LLM-Based Document Analysis and Comparison Application

## Project Overview

The Document Portal is an LLM (Large Language Model) based application designed to facilitate intelligent interaction with documents. It provides a comprehensive suite of features for document analysis, conversational querying, and comparison, leveraging various LLM and embedding models.

## Key Features

*   **Document Analysis Agent**: Analyze uploaded documents to extract key insights, summaries, and structured information.
*   **Chat Agent**: Engage in conversational interactions with the application to understand document content, ask questions, and retrieve specific information.
*   **Comparison Agent**: Compare multiple uploaded files to identify similarities, differences, and relationships between their contents.

## Local Development Setup

To set up the project locally, follow these steps:

1.  **Create a Conda Environment**:
    ```bash
    conda create -p env python=3.10 -y
    conda activate ./env
    ```

2.  **Install Dependencies**:
    Ensure you have a `requirements.txt` file in your project root.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application (Local Development Mode)**:
    For local development with hot-reloading:
    ```bash
    uvicorn api.main:app --reload --host 0.0.0.0 --port 8089
    ```
    Access the application in your browser at `http://localhost:8089`.

## Docker Setup

This project includes a `Dockerfile` and a `Makefile` to facilitate building and running the application using Docker.

1.  **Build the Docker Image**:
    ```bash
    make build
    ```
    This command builds a Docker image named `fastapi-app`.

2.  **Run the Docker Container**:
    ```bash
    make run
    ```
    This command runs the Docker container in detached mode, mapping port 8089 from the container to your host machine. You can access the application at `http://localhost:8089` in your browser.

3.  **Stop the Docker Container**:
    ```bash
    make stop
    ```
    This command stops and removes the running Docker container.

4.  **Clean Docker Resources**:
    ```bash
    make clean
    ```
    This command stops and removes the container, and then removes the Docker image.

## AWS ECS and Fargate Integration (CI/CD)

This project is configured for continuous deployment to AWS ECS Fargate using GitHub Actions.

*   **`template.yml`**: An AWS CloudFormation template that defines the necessary AWS infrastructure (ECR, VPC, Subnets, ECS Cluster, Task Definition, Service, IAM Roles, Security Groups) for deploying the application.
*   **`aws.yml`**: A GitHub Actions workflow that automates the build, tag, and push of the Docker image to ECR, and then deploys the updated ECS Task Definition and Service. This workflow is triggered on pushes to the `main` branch.
*   **`task_definition.json`**: A base ECS Task Definition JSON file that is updated by the GitHub Actions workflow with the latest Docker image URI before deployment.

**Deployment Steps:**

1.  **Configure AWS Secrets in GitHub**:
    *   In your GitHub repository, go to `Settings` > `Secrets and variables` > `Actions`.
    *   Add two new repository secrets:
        *   `AWS_ACCESS_KEY`: Your AWS IAM user's access key ID.
        *   `AWS_SECRET_ACCESS_KEY`: Your AWS IAM user's secret access key.
    *   Ensure this IAM user has permissions to interact with ECR, ECS, CloudFormation, and IAM.

2.  **Push to `main` Branch**:
    *   Push your code changes to the `main` branch of your GitHub repository. This will automatically trigger the GitHub Actions workflow.

3.  **Monitor GitHub Actions**:
    *   Go to the "Actions" tab in your GitHub repository.
    *   Monitor the "Deploy to Amazon ECS" workflow run for successful completion. Review logs for any failures.

4.  **Verify Deployment in AWS Console**:
    *   **CloudFormation**: Check for the `ecr-repo-stack` in CloudFormation (if deployed by the workflow).
    *   **ECR**: Verify your Docker image is pushed to the `documentportal` repository.
    *   **ECS**: Confirm that `document-portal-cluster` and `document-portal-service` are running, and a task is in `RUNNING` state.
    *   **CloudWatch**: Check logs in `/ecs/documentportaltd` for application output.

5.  **Access Deployed Application**:
    *   Retrieve the Public IP address of your running ECS task from the ECS console.
    *   Access the application in your browser at `http://<Public_IP_Address>:8080`.

## LLM and Embedding Models

The project supports integration with various Large Language Models (LLMs) and Embedding Models:

### Supported LLM Models:

*   **Groq**: Freely available.
*   **OpenAI**: Paid service.
*   **Gemini**: Offers a 15-day free access period.
*   **Claude**: Paid service.
*   **Hugging Face**: Freely available models.
*   **Ollama**: For local model setup.

### Supported Embedding Models:

*   **OpenAI**
*   **Hugging Face**
*   **Gemini**

### Vector Database Options:

*   In-memory
*   On-disk
*   Cloud-based