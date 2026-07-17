---
layout: post
title: "Updating Gen3 Dictionary"
date: 2026-03-13
author: LT
categories: msu-gen3-dictionaries
---

## Overview

This guide walks through the process of updating a Gen3 Data Dictionary locally using Docker and the msu-gen3-dictionaries repository. The workflow enables you to develop, test, and validate dictionary changes before pushing to production.

## Prerequisites

- Docker Desktop (v3.2.1 or later)
- GNU Make
- Git

### Installing Make on Windows

Make is pre-installed on Linux and macOS. On Windows, you will need to install it manually:

1. Run the following in PowerShell as Administrator:

```powershell
winget install ezwinports.make
```

## Step-by-Step Workflow

### 1. Clone the Repository

Clone the msu-gen3-dictionaries repository from GitHub:

```bash
git clone https://github.com/naultran/msu-gen3-dictionaries
cd msu-gen3-dictionaries
```

### 2. Create a Feature Branch

Create a new branch for your changes:

```bash
git checkout -b feature/your-dictionary-changes
```

### 3. Edit the Dictionary Schema

Modify the YAML files in the `dictionary/` directory. For example:
- `dictionary/pvatppg/` for PVATPPG schema
- `dictionary/toxdatacommons/` for ToxDC schema

### 4. Pull Docker Images

Download the latest Docker images:

```bash
make pull
```

### 5. Start Containers

Launch the Docker containers in the background:

```bash
make up
```

This starts all services including the visualization server on port 80.

### 6. Compile the Dictionary

Compile your schema changes into JSON format. This replaces the json file in msu-gen3-dictionaries/schema/:

```bash
make compile dd=pvatppg
```

Replace `pvatppg` with your target dictionary (`toxdatacommons`, etc.).

### 7. Verify in Browser

Open your browser and visit one of these URLs:

- `http://localhost/#schema/pvatppg.json`
- `http://localhost/#schema/toxdatacommons.json`

Verify that the dictionary visualization looks correct.

### 8. Push Changes

Commit and push your branch to the remote repository:

```bash
git add .
git commit -m "Update dictionary schema"
git push origin feature/your-dictionary-changes
```

### 9. Create a Pull Request

Create a pull request on GitHub to merge your changes into the main branch.

### 10. Merge and Clean Up

Merge the pull request:

```bash
git checkout main
git pull origin main
git branch -d feature/your-dictionary-changes
git push origin --delete feature/your-dictionary-changes
```
### Note:

Updates to the remote GitHub repository do not automatically trigger updates to the website. Follow the instructions located here to update the website after changes are made to the msu-gen3-dictionaries repository: https://github.com/Nault-lab/gen3-gitops/blob/main/sop/data-dictionary-update.md

## Troubleshooting

### 404 Error When Accessing Schema

**Problem:** Getting `GET http://localhost/schema/pvatppg [HTTP/1.1 404 Not Found]`

**Solution:** Ensure the schema file exists:

```bash
docker exec ddvis ls -la /usr/share/nginx/html/schema/
```

The file should be named with the `.json` extension (e.g., `pvatppg.json`). If missing, run:

```bash
make compile dd=pvatppg
```

Then restart the containers:

```bash
make restart
```

### JSON Parse Error

**Problem:** `SyntaxError: JSON.parse: unexpected character`

**Solution:** The schema file wasn't found (404 error), so the browser received an error page instead of JSON. Follow the steps above to ensure the schema file exists.

### Containers Won't Start

**Problem:** `docker compose up` fails

**Solution:**

1. Check .env file exists (or use .env-sample):
   ```bash
   ls -la .env
   ```

2. Load environment variables:
   ```bash
   make up
   ```

3. Check container status:
   ```bash
   docker compose ps
   ```

### Port 80 Already in Use

**Problem:** Another service is using port 80

**Solution:** Modify `docker-compose.yml` or `docker-compose.override.yml` to use a different port (e.g., 8080):

```yaml
services:
  ddvis:
    ports:
      - "8080:80"
```

Then access at `http://localhost:8080`

## Useful Commands

| Command | Purpose |
|---------|---------|
| `make pull` | Download latest Docker images |
| `make up` | Start all containers |
| `make down` | Stop all containers |
| `make restart` | Restart containers |
| `make ps` | Show container status |
| `make compile dd=pvatppg` | Compile dictionary to JSON |
| `make test dd=pvatppg` | Run validation tests |
| `make psql` | Connect to PostgreSQL database |

## Related Resources

- [Gen3 Official Documentation](https://gen3.org)
- [umccr-dictionary Repository](https://github.com/umccr/umccr-dictionary)
- [Gen3 Data Dictionary Guide](https://github.com/uc-cdis/datadictionary)

## Notes

This workflow supersedes the outdated "dumpschema.py" method.
