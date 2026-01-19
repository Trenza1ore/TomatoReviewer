# Tomato Review

Python code review agent using pylint and PEP knowledge base.

## Installation

With `pip`:
```bash
uv pip install git+https://gitcode.com/SushiNinja/TomatoReviewer.git@main
```

Same with `uv`:
```bash
uv pip install git+https://gitcode.com/SushiNinja/TomatoReviewer.git@main
```

## Usage

```bash
# Review all Python files in current directory
tomato-review *.py

# Review specific files
tomato-review file1.py file2.py

# Review all Python files in src/ recursively
tomato-review src/**/*.py

# Review without applying fixes
tomato-review *.py --no-fix

# Review with custom maximum iterations
tomato-review *.py --max-iter 5

# Review with custom mini batch size
tomato-review *.py --mini-batch 10

# Rebuild Knowledge Base even if it exists
tomato-review *.py --rebuild

# Use custom config file
tomato-review *.py --config-file /path/to/config.yaml
```

### Command-line Options

- `-h, --help`: Show help message and exit
- `-m MAX_ITER, --max-iter MAX_ITER`: Maximum iterations of file fixing (default: 10)
- `-b MINI_BATCH, --mini-batch MINI_BATCH`: Mini batch size for files to process at the same time (default: 20)
- `--no-fix`: Only review files without applying fixes
- `--rebuild`: Rebuilds Knowledge Base even if it exists
- `--config-file CONFIG_FILE`: Path to config file (tomato.yaml, .tomato.yaml, or pyproject.toml)

## Configuration

Create a `.tomato.yaml`, `tomato.yaml`, or add configuration to `pyproject.toml` in your project root. The following is an example configuration - adjust the values to match your setup:

```yaml
tomato-review:
  kb_id: "edinburgh"
  milvus_uri: "http://your-milvus-host:19530"  # Update with your Milvus server URI
  milvus_token: ""  # Add your Milvus token if required
  database_name: "pep_kb"
  embedding_model_name: "your-embedding-model"  # Update with your embedding model name
  embedding_api_key: "sk-********************"  # Update with your API key
  embedding_base_url: "http://your-embedding-server/v1/embeddings"  # Update with your embedding API URL
  chunk_size: 512
  chunk_overlap: 128
  index_type: "hybrid"
  api_base: "http://your-api-server/v1/"  # Update with your LLM API server URL
  api_key: "sk-********************"  # Update with your LLM API key
  model_name: "your-model-name"  # Update with your LLM model name
  model_provider: "OpenAI"
  verify_ssl: false
  ssl_cert: null
```

## Output

- **Reviews**: `tomato/reviews/` - Markdown review reports
- **Backups**: `tomato/backup/` - Original files before modification
- **Logs**: `tomato/logs/` - Processing logs for each file

Files are modified in place after review and fixing.
