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
