# Cloud DevOps Task API

A containerized Python REST API demonstrating DevOps and Site Reliability Engineering practices.

## Technologies

- Python
- FastAPI
- Docker
- Git & GitHub
- GitHub Actions
- Pytest
- Prometheus
- REST API
- Application Logging

## Features

- REST API endpoints
- Automated API testing
- Docker containerization
- Docker health checks
- CI/CD using GitHub Actions
- Application request logging
- Prometheus metrics and observability

## API Endpoints

### GET /

Returns the application status.

### GET /health

Returns the health status of the application.

### GET /metrics

Exposes Prometheus metrics including request count, response size, and request latency.

## CI/CD Pipeline

Every push to the `main` branch triggers GitHub Actions to:

1. Check out the source code
2. Set up Python
3. Install dependencies
4. Run automated tests
5. Build the Docker image

## Docker

The application runs on port `8000`.

The Docker container includes a health check that continuously verifies the `/health` endpoint.

## Monitoring

Prometheus instrumentation exposes application metrics through `/metrics`.

Application logs record:

- Request method
- Request path
- HTTP status code
- Request start and completion

## Project Goal

This project demonstrates practical DevOps/SRE concepts including CI/CD, containerization, health monitoring, logging, automated testing, and application observability.# Cloud DevOps Task API

A containerized Python REST API demonstrating DevOps and Site Reliability Engineering practices.

## Technologies

- Python
- FastAPI
- Docker
- Git & GitHub
- GitHub Actions
- Pytest
- Prometheus
- REST API
- Application Logging

## Features

- REST API endpoints
- Automated API testing
- Docker containerization
- Docker health checks
- CI/CD using GitHub Actions
- Application request logging
- Prometheus metrics and observability

## API Endpoints

### GET /

Returns the application status.

### GET /health

Returns the health status of the application.

### GET /metrics

Exposes Prometheus metrics including request count, response size, and request latency.

## CI/CD Pipeline

Every push to the `main` branch triggers GitHub Actions to:

1. Check out the source code
2. Set up Python
3. Install dependencies
4. Run automated tests
5. Build the Docker image

## Docker

The application runs on port `8000`.

The Docker container includes a health check that continuously verifies the `/health` endpoint.

## Monitoring

Prometheus instrumentation exposes application metrics through `/metrics`.

Application logs record:

- Request method
- Request path
- HTTP status code
- Request start and completion

## Project Goal

This project demonstrates practical DevOps/SRE concepts including CI/CD, containerization, health monitoring, logging, automated testing, and application observability.