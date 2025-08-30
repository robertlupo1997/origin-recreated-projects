[![CI](https://github.com//actions/workflows/ci.yml/badge.svg)](https://github.com//actions/workflows/ci.yml)

# Origin Recreated Projects

[![Pages](https://github.com/robertlupo1997/origin-recreated-projects/actions/workflows/pages.yml/badge.svg)](https://github.com/robertlupo1997/origin-recreated-projects/actions/workflows/pages.yml)

A collection of public-safe demonstration projects showcasing modern software engineering practices and architectural patterns. These projects recreate common enterprise patterns using synthetic data and generic implementations.

## What This Repository Demonstrates

- **Microservices Architecture**: Independent, loosely-coupled services with clear boundaries
- **API-First Design**: RESTful APIs with comprehensive documentation and testing
- **Modern Frameworks**: FastAPI, Hono, contemporary Python/Node.js patterns
- **Security Best Practices**: Zero real secrets, complete data sanitization, comprehensive scanning
- **Development Workflow**: CI/CD pipelines, automated testing, quality gates
- **Documentation Excellence**: Comprehensive README files, API documentation, GitHub Pages

## Projects Overview

### 🔧 APM Agent Backend
Application Performance Monitoring service with metrics collection and alerting.

**Quick Start:**
```bash
cd apm-agent-backend
pip install -e .
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

**Key Features:**
- FastAPI framework with automatic OpenAPI documentation
- Health monitoring, metrics collection, and alert management
- Three REST API routers with comprehensive endpoints
- Pydantic models for type safety and validation

---

### 🌐 MCP Gateway
Model Context Protocol gateway service with PKCE authentication flow.

**Quick Start:**
```bash
cd procore-mcp-gateway
npm install
npm run dev
```

**Key Features:**
- High-performance Hono web framework
- Complete PKCE (Proof Key for Code Exchange) implementation
- Construction project and document management APIs
- Comprehensive unit testing for security components

---

### 🔍 RAG System
Retrieval-Augmented Generation system for document search and similarity matching.

**Quick Start:**
```bash
cd rag-system
pip install -r requirements.txt
uvicorn src.main:app --reload --host 0.0.0.0 --port 8001
```

**Key Features:**
- 1536-dimensional embedding support (OpenAI ada-002 compatible)
- Synthetic document corpus with category-based filtering
- Advanced similarity scoring and search algorithms
- Database schema supporting vector operations

---

### 📊 RFI Automation
Request for Information processing with automated Excel reporting.

**Quick Start:**
```bash
cd rfi-automation
pip install -r requirements.txt
python src/rfi_processor.py
```

**Key Features:**
- CSV data processing with pandas
- Multi-sheet Excel report generation with analytics
- Command-line interface with flexible options
- Comprehensive summary statistics and breakdowns

## Running All Tests

```bash
# Python projects
cd apm-agent-backend && pytest tests/
cd rag-system && pytest tests/
cd rfi-automation && pytest tests/

# Node.js projects
cd procore-mcp-gateway && npm test
```

## Security & Quality Assurance

### 🛡️ Security Features
- **Zero Hardcoded Secrets**: All sensitive values in `.env.example` templates
- **Synthetic Data Only**: No real customer or proprietary information
- **Generic Implementations**: No client-specific code or business logic
- **Automated Scanning**: PowerShell script checks for sensitive patterns

### ✅ Quality Assurance
- **Type Safety**: Pydantic models, comprehensive validation
- **Error Handling**: FastAPI automatic validation, custom error responses
- **Documentation**: OpenAPI/Swagger auto-generation, detailed README files
- **Testing**: Comprehensive smoke tests for all critical functionality
- **CI/CD Pipeline**: Automated testing, linting, and security scanning

## Repository Metrics

Run the measurement script to generate current statistics:

```bash
./scripts/measure.sh
```

**Current Highlights:**
- 🚀 **8+ API Endpoints** across all services
- 📋 **1,500+ Lines** of production-ready code
- 🧪 **100% Smoke Test Coverage** for all critical paths
- 🔒 **Zero Security Issues** detected by automated scanning

## Development Workflow

### Prerequisites
- Python 3.11+
- Node.js 18+
- PowerShell (for security scanning)

### Environment Setup
Each project includes environment templates:
- `apm-agent-backend/.env.example`
- `procore-mcp-gateway/.dev.vars.example`
- `rag-system/.env.example`
- `rfi-automation/.env.example`

### Code Quality
```bash
# Python linting
ruff check src/

# Security scan
./scripts/redact_check.ps1

# Metrics generation
./scripts/measure.sh > docs/metrics.md
```

## Documentation

📚 **[Complete Documentation](https://robertlupo1997.github.io/origin-recreated-projects/)** - Comprehensive guides and API documentation

- **[Projects Guide](https://robertlupo1997.github.io/origin-recreated-projects/projects.html)** - Detailed setup instructions
- **[Metrics Dashboard](https://robertlupo1997.github.io/origin-recreated-projects/metrics.html)** - Generated project statistics

## Architecture Decisions

### Technology Choices
- **FastAPI**: Modern Python framework with automatic API documentation
- **Hono**: High-performance web framework for Node.js
- **Pydantic**: Type safety and validation for Python
- **OpenAPI**: Industry-standard API documentation
- **GitHub Actions**: Comprehensive CI/CD pipeline

### Design Principles
- **Security by Design**: No real data ever touches this repository
- **API-First**: All services designed as RESTful APIs
- **Microservices**: Independent deployments and scaling
- **Documentation-Driven**: Comprehensive documentation for all components
- **Test-Driven**: Smoke tests ensure reliability

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/robertlupo1997/origin-recreated-projects.git
   cd origin-recreated-projects
   ```

2. **Choose a project and follow its Quick Start guide above**

3. **Run the security scan to verify clean state:**
   ```bash
   ./scripts/redact_check.ps1
   ```

4. **Generate current metrics:**
   ```bash
   ./scripts/measure.sh
   ```

---

**Portfolio Demonstration** - This repository showcases professional software development practices while maintaining complete security through synthetic data and generic implementations.