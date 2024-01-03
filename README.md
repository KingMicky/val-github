# Valentine API

The Valentine API is a simple Flask web application designed for Valentine's Day. It provides romantic and non-romantic quotes and allows users to answer the question, "Will you be my Valentine?"

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [Endpoints](#endpoints)
- [Docker](#docker)

## Features

- Display romantic and non-romantic quotes.
- Allow users to respond to the question "Will you be my Valentine?".

## Getting Started

### Prerequisites

- Python (3.8 or higher)
- Pytest
- pip
- Docker (optional)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/valentine-api.git
   cd valentine-api

2. Install Dependency:

   ```bash
   pip install pytest 
   pip install flask

3. Usage:

   ```bash
    python valentine_api.py

4. Docker:

    ```bash
    docker build -t valentine-api .
    docker run -d -p 80:80 valentine-api
