# CyberLab

**CyberLab** is an interactive cybersecurity learning platform designed to provide hands-on experience through isolated, containerized security labs.

The platform allows users to launch vulnerable environments, practice cybersecurity techniques, complete security challenges, and automatically generate structured reports based on their laboratory activities.

Unlike traditional cybersecurity training platforms, CyberLab focuses not only on solving security challenges but also on **understanding, documenting, and reporting security vulnerabilities**, helping users develop practical skills used in real-world security assessments.

## Planned Features

- **Containerized Security Labs** – Launch isolated, vulnerable environments on demand using Docker.
- **Interactive Challenges** – Practice identifying, analyzing, and exploiting vulnerabilities in authorized lab environments.
- **Automated Lab Management** – Dynamically create, monitor, stop, and remove containers.
- **Browser-Based Lab Access** – Access laboratory environments directly through the web interface.
- **Automated Security Reports** – Generate structured reports containing discovered vulnerabilities, technical findings, and remediation recommendations.
- **Progress Tracking** – Monitor completed labs, challenge results, and learning progress.
- **Resource Management** – Enforce resource limits and automatically terminate expired laboratory sessions.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Containerization | Docker |
| Container Management | Docker SDK for Python |
| Communication | REST API, WebSockets |
| Report Generation | Python-based reporting system |

## How It Works

1. **Select a Lab** – The user chooses a cybersecurity challenge from the available laboratory catalog.
2. **Launch Environment** – The backend creates an isolated Docker container containing the selected vulnerable environment.
3. **Access the Lab** – The user connects to the environment and begins investigating the security challenge.
4. **Complete the Challenge** – The platform tracks the laboratory session and records relevant results.
5. **Generate a Report** – CyberLab generates a structured security assessment report using collected evidence and submitted findings.
6. **Terminate Environment** – The platform stops and removes the container, releasing allocated resources.

## Project Architecture

CyberLab follows a full-stack architecture consisting of:

- **Frontend:** A React application providing the user interface, laboratory management, and progress visualization.
- **Backend:** A FastAPI service responsible for authentication, laboratory orchestration, challenge validation, and report generation.
- **Database:** PostgreSQL stores user information, laboratory configurations, active sessions, and assessment results.
- **Docker Engine:** Runs and manages isolated laboratory environments.

## Shared Platform and Isolated Lab Sessions

CyberLab uses a shared platform database and separate Docker environments
for individual laboratory sessions.

### Shared Platform Database

A single PostgreSQL database stores:

- Users.
- The laboratory catalog and Docker image references.
- Laboratory session records.
- Per-user laboratory completions and learning progress.
- Assessment findings and reports as these features are implemented.

The laboratory catalog is shared across users. Session records, progress,
findings, and reports are associated with their respective users and are
subject to access controls.

Backend requests access this same database through separate SQLAlchemy
sessions and transactions. A SQLAlchemy session does not create a separate
database or a laboratory environment.

### Laboratory Images and Instances

Each laboratory is defined by a Docker image containing its initial
environment, application, files, and intended vulnerabilities.

Starting a laboratory creates a new container from the configured image
for that laboratory session.

If two users start the same laboratory, CyberLab creates two separate
containers from the same image. Users do not share a running laboratory
container, and changes made in one session must not affect another.

Any writable volumes, databases, or supporting services required by a
laboratory must also be isolated per session. Laboratory environments
must not have access to the platform database or the Docker socket.

A laboratory requiring multiple containers will receive a separate set
of containers and an isolated network for each session.

### Session Lifecycle

The backend will:

1. Resolve the selected laboratory from the shared catalog.
2. Create an isolated environment and record its association with the
   user and laboratory.
3. Provide access to that environment.
4. Track its lifecycle and enforce resource limits and expiration.
5. Stop and remove the environment and its temporary resources when
   the session ends or expires.

Starting or stopping a session does not automatically mark a laboratory
as completed. Completion is recorded separately after challenge validation.

### Development Scope

The initial implementation will use one predefined local user.
Authentication and multi-user access controls are deferred.

The shared database and isolated laboratory session model remain the
target architecture as multi-user support is introduced.

## Security Considerations

CyberLab is intended exclusively for educational and authorized security testing.

Laboratory environments will be configured with resource restrictions, network isolation, session expiration policies, and additional sandboxing controls where necessary.

## Project Status

🚧 **Under Development**

CyberLab is currently in its initial development phase. Features and architecture may evolve throughout implementation.

## Project Goals

- Provide accessible, practical cybersecurity training.
- Explore dynamic container orchestration using Docker.
- Automate the lifecycle of vulnerable laboratory environments.
- Introduce structured security reporting into hands-on learning.
- Develop a scalable and maintainable full-stack application.

## Disclaimer

CyberLab is intended for educational purposes only. All cybersecurity exercises must be performed within authorized and isolated environments. The project does not encourage unauthorized access to external systems.

## License

This project is planned to be released under the MIT License.
