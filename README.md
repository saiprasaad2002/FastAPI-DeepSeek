# FastAPI Code Generation with Deepseek-R1

This repository provides a FastAPI-based API endpoint that leverages the Deepseek-R1 LLM to generate Python code from natural language descriptions of business use cases.  It demonstrates how to use LLMs for automated code generation within a structured application framework.

## Overview

This project exposes a single API endpoint (`/deepseek-r1`) that accepts a textual description of a business use case as input.  It then uses the Deepseek-R1 LLM to generate Python code implementing that use case, following a predefined file structure and incorporating best practices like try-except blocks.

## Features

* Automated Python code generation from natural language descriptions.
* FastAPI framework for API endpoint.
* Deepseek-R1 LLM integration.
* Structured code output following a specific file organization.
* Inclusion of try-except blocks for error handling.

## Technologies Used

* **API Framework:** FastAPI
* **Large Language Model (LLM):** Deepseek-R1
* **LLM Interaction:** `ollama` Python library
* **Dependencies:** `fastapi`, `pydantic`, `uvicorn`, `ollama` (list all dependencies in `requirements.txt`)

## Install dependencies:

Bash

python -m venv venv  # Create a virtual environment (recommended)
source venv/bin/activate  # Activate (Linux/macOS)
venv\Scripts\activate  # Activate (Windows)
pip install -r requirements.txt  # Install all project dependencies

## Start Ollama:
Ensure you have Ollama running and the deepseek-r1:1.5b model available. Refer to the Ollama documentation for installation and model management.
