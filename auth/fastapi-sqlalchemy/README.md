# Basic Auth API using FastAPI and SQLAlchemy

## Getting Started

### Prerequisites

- Python 3.7+
- MySQL

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ph10012479/boilerplate.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add the following variables:

```bash
DATABASE_URL=mysql+pymysql://<username>:<password>@127.0.0.1:3306/auth
```

4. Run the server:

```bash
python server.py
```

5. Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation.
