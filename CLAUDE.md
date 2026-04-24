# Claude Code Starter — Project Conventions

## Language & Runtime
- Python 3.11+
- All source code lives in `src/`, tests in `tests/`, prompts in `prompts/`

## Code Style
- Follow PEP 8; keep functions small and single-purpose
- Use type hints on all function signatures
- No comments unless the WHY is non-obvious
- No unused imports or dead code

## Testing
- Use pytest; every public function must have at least one test
- Run tests with: `pytest`
- Tests must pass before committing

## Environment
- Copy `.env.example` to `.env` and fill in real values; never commit `.env`
- Load env vars with `python-dotenv`

## Git
- Branch from `main` for each feature; use descriptive branch names
- Commit messages: short imperative summary (<72 chars)
- Push and open a PR; do not merge without passing CI
