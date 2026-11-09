# From Git to Gold — FreshCart Pipelines

Data Engineering assignment starter repository.

## Project structure

- `elt/` — FreshCart ELT notebook and notes (Part B)
- `iris_project/` — Mage Iris ML pipeline (Part C)
- `stream/` — RabbitMQ dispatcher and driver (Part D)
- `tests/` — pytest tests
- `.github/workflows/ci.yml` — GitHub Actions CI workflow

## Local setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

## Git workflow

```bash
git init
git add .
git commit -m "Initial project structure"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/freshcart-pipelines.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your GitHub username.

## Important

Do not commit `.env`, credentials, API keys, Snowflake connection details,
generated `.csv` files, model `.pkl` files, or logs. Keep secrets in environment
variables or a local `.env` file that is ignored by Git.
