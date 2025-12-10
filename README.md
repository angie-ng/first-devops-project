# DafneApp
DafneApp is a simple Python Flask application used to demonstrate a full CI/CD workflow with Docker, Docker Compose, GitHub Actions, Traefik reverse proxy, and automated deployment to a production server.
The application exposes an endpoint (`/health`) that returns a simple JSON response. JSON is used because it is a standard format for REST APIs, which makes the service easy to test, monitor, and extend in the future.

---

## Tech Stack
- **Python + Flask**
- **Docker + Docker Compose**  
- **GitHub Actions (CI/CD)** 
- **GHCR (GitHub Container Registry)**
- **Traefik (reverse proxy + HTTPS)**
- **Oracle Cloud (production server)**

---

## Architecture Overview
- The Flask application runs inside a Docker container.
- The GitHub Actions CI workflow builds the Docker image, tests it and pushes it to GHCR.
- The CD GitHub Actions workflow acts as a trigger. It connects to the production server via SSH and runs a local deployment script `deploy.sh`.
The script performs the actual deployment steps: logging into GHCR, pulling the new image, and applying the updated Docker Compose configuration.
- Traefik manages routing, HTTPS certificates (Let's Encrypt), and exposes the application under:
  - `https://dafneapp.eu`
  - `https://www.dafneapp.eu`
 
---

## Running locally
1. Clone the repository
   `git clone https://github.com/angie-ng/first-devops-project.git`
   `cd first-devops-project`
2. Run the app with Docker Compose
   `docker compose up --build`

   Optional: Run on the background
   `docker compose up --build -d`
3. Check the health endpoint
   `curl http://127.0.0.1:5000/health`
   Expected response: `{"message": "Hello World!"}`

---

## CI/CD Workflow Explanation
### Continuous Integration (CI)
The trigger for CI workflow (`ci.yml`) is a push or pull request to the `main` branch on Github.
Steps:
1. **Checkout repository** - this step downloads the code from the repository to the GitHub Actions runner (from now on just "runner") so that CI/CD can use it.
2. **Python setup** - sets up Python on the runner, installs dependencies, and prepares the environment for testing.
3. **Build local Docker image** - builds a Docker image locally on the runner for testing purposes only.
4. **Smoke test of the Docker container** - verifies that the container runs correctly by sending a request to the `/health` endpoint.
5. **Log in to GHCR (GitHub Container Registry)** - authenticates using the GitHub token to allow pushing Docker images.
6. **Build and push final Docker image for production** - builds a Docker image intended for production, tags it with a unique hash corresponding to the triggering commit, and pushes it to GHCR. The image tag is exported so that the CD workflow (or other jobs) can reference the correct image.
7. **Run container on Github runner using Docker compose** - optional staging deployment using Docker Compose at the end of the CI workflow.
