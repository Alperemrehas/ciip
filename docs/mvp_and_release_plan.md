# CIIP MVP and Release Plan

## Project Name

**Capability Interoperability Intelligence Platform — CIIP**

## Current Release Target

**CIIP v0.1 — Interoperability Analytics MVP**

## Product Summary

CIIP is an open-source interoperability intelligence and analytics platform.

CIIP does **not** execute interoperability tests. Instead, tests are performed in an external/common testing platform used by participating organizations. CIIP imports those external test results, normalizes them, maps them to companies, industries, capabilities, systems, scenarios, test cases, interoperability layers, and years, then provides analytics, scoring, dashboards, gap analysis, and reports.

The main goal is to help organizations understand:

* which companies tested with which companies
* in which industries
* for which capabilities
* using which systems
* in which year or project cycle
* which interoperability layers were successful or weak
* which gaps are persistent across years
* which capabilities were added, missing, repeated, or untested
* whether companies are improving interoperability or repeatedly testing with the same partners

## What CIIP Is

CIIP is:

* an interoperability intelligence platform
* a multi-year interoperability analytics tool
* a capability mapping and assessment platform
* a test-result normalization platform
* a gap analysis and reporting platform
* a strategic planning support tool for future interoperability improvement

## What CIIP Is Not

CIIP is not:

* a test execution platform
* an API testing tool
* a replacement for Postman, JMeter, Selenium, or similar tools
* an enterprise service bus
* an integration broker
* a live data exchange platform
* a real-time monitoring platform
* a production identity and access management system in v0.1

## Core Concept

The platform follows this core model:

```text
Company
  → Industry
    → Capability
      → System/Application
        → External Test Result
          → Analytics / Score / Gap / Report
```

A company can operate in multiple industries.

A company can have multiple capabilities within each industry.

The same company can test different capabilities in different years.

The same pair of companies can test the same or different capabilities across multiple years.

## Example Scenario

Alpha Group operates in logistics, healthcare, and advertising.

In 2024:

* Alpha Group tests Logistics / Inventory Visibility with Beta Nexus.
* The main gap is semantic data mismatch.

In 2025:

* Alpha Group repeats Logistics / Inventory Visibility with Beta Nexus.
* Alpha Group adds Healthcare / Patient Data Exchange with Gamma Works.

In 2026:

* Alpha Group improves logistics interoperability with Beta Nexus.
* Alpha Group adds Advertising / Campaign Analytics with Gamma Works.
* Some declared capabilities remain untested.
* The platform detects repeated partner concentration and persistent semantic gaps.

CIIP should analyze this pattern and show what improved, what is missing, and what should be prioritized next.

---

# MVP v0.1 Scope

## MVP Objective

The v0.1 objective is to build a working local platform that can:

1. store companies, industries, capabilities, systems, projects, scenarios, and test cases
2. import external test results from CSV or Excel
3. normalize imported results
4. calculate interoperability scores
5. analyze multi-year trends
6. detect gaps, missing coverage, and repeated testing patterns
7. expose dashboard-ready API endpoints
8. provide an initial Streamlit dashboard
9. prepare the foundation for future AI-assisted reporting

## In-Scope Features for v0.1

### 1. Backend Foundation

* FastAPI application
* PostgreSQL database
* SQLAlchemy 2.0 ORM
* Pydantic schemas
* Alembic migrations
* Docker Compose local development
* Health endpoint
* Basic project structure
* Basic automated tests

### 2. Master Data Management

The platform should support CRUD operations for:

* companies
* industries
* capabilities
* systems/applications
* projects
* project cycles/years
* scenarios
* test cases
* interoperability layers

### 3. Company-Industry-Capability Mapping

The platform must support:

* companies operating in multiple industries
* capabilities belonging to industry context
* companies declaring capabilities per industry
* systems/applications associated with company capabilities
* yearly capability snapshots

Example:

```text
Company: Alpha Group
Industry: Logistics
Capability: Inventory Visibility
System: SAP ERP
Year: 2024
```

### 4. External Result Import

The platform should import CSV and Excel files from an external testing platform.

The canonical import schema should include:

```text
external_test_id
project_name
cycle_year
scenario_name
test_case_code
test_case_name
test_date

source_company
source_industry
source_capability
source_system

target_company
target_industry
target_capability
target_system

layer
outcome
severity
gap_type
gap_summary
recommendation
evidence_uri
```

Required fields:

```text
external_test_id
project_name
cycle_year
scenario_name
test_case_code
test_case_name
test_date
source_company
source_industry
source_capability
target_company
target_industry
target_capability
layer
outcome
```

Optional fields:

```text
source_system
target_system
severity
gap_type
gap_summary
recommendation
evidence_uri
```

### 5. Raw and Normalized Data Storage

The platform must preserve both:

* raw imported rows
* normalized canonical records

This supports traceability, debugging, and auditability.

### 6. Import Validation

The import pipeline should validate:

* file type
* required columns
* invalid year values
* invalid outcome values
* invalid layer values
* missing companies
* missing industries
* missing capabilities
* duplicate external test IDs
* inconsistent source/target mappings

The import should produce:

* total rows
* accepted rows
* rejected rows
* warning count
* error count
* validation messages

### 7. Outcome Normalization

Supported outcomes:

```text
PASS
PARTIAL_PASS
FAIL
BLOCKED
NOT_TESTED
NOT_APPLICABLE
```

Default score mapping:

```text
PASS = 1.00
PARTIAL_PASS = 0.50
FAIL = 0.00
BLOCKED = 0.00
NOT_TESTED = null / excluded
NOT_APPLICABLE = null / excluded
```

### 8. Interoperability Layers

Supported interoperability layers:

```text
LEGAL — Legal interoperability
ORG   — Organisational / business process interoperability
SEM   — Semantic / data interoperability
TECH  — Technical / protocol interoperability
SEC   — Security / identity interoperability
GOV   — Governance / agreement interoperability
```

Every normalized test result should be mapped to one layer.

### 9. Scoring Engine

The v0.1 scoring engine should calculate:

* company pair score
* company-year score
* industry score
* capability score
* layer score
* project cycle score
* company capability coverage score
* partner diversity score
* repeated partner concentration
* persistent gap indicators

### 10. Analytics Engine

The v0.1 analytics engine should provide data for:

* overview KPIs
* company-to-company interoperability matrix
* year-over-year score trend
* capability coverage by company
* declared-but-untested capabilities
* new capabilities by year
* repeated capabilities by year
* missing/disappeared capabilities
* industry score comparison
* interoperability layer breakdown
* outcome distribution
* partner diversity analysis
* repeated partner concentration
* gap frequency
* persistent gaps
* company profile analytics
* company pair analytics
* project/year analytics

### 11. Dashboard

The first dashboard can be built with Streamlit.

Initial pages:

1. Overview
2. Import Center
3. Master Data
4. Company Analysis
5. Pair Analysis
6. Industry Analysis
7. Capability Analysis
8. Gap Analysis
9. Reports

For v0.1, the minimum acceptable pages are:

1. Overview
2. Import Center
3. Company Analysis
4. Capability Coverage
5. Gap Analysis

### 12. Reports

Initial report generation should include:

* executive summary
* key KPIs
* year-over-year trend
* strongest interoperability relationships
* weakest interoperability relationships
* new capabilities
* missing/untested capabilities
* repeated partner risks
* persistent gaps
* recommendations for next year

In v0.1, reports may be generated as HTML or Markdown. PDF export can come later.

### 13. Optional AI Summary

AI integration is optional in v0.1.

If implemented, AI must not calculate deterministic scores. AI should only summarize already computed analytics.

Acceptable AI use cases:

* executive summary generation
* gap explanation
* recommendation drafting
* report narrative generation
* next-year priority suggestions

AI input should be structured analytics JSON, not uncontrolled raw data.

AI output should be stored and auditable.

---

# Out of Scope for v0.1

The following features are explicitly out of scope for v0.1:

* executing tests inside CIIP
* live SAP/API/system integration testing
* real-time test monitoring
* SSO
* production RBAC
* Kubernetes deployment
* multi-tenant production hardening
* advanced evidence file security
* automatic protocol scanning
* automatic API conformance testing
* machine learning prediction
* graph database
* vector database
* complex workflow engine
* production-grade React frontend
* public SaaS deployment

---

# Technical Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy 2.0
* Pydantic
* Alembic
* PostgreSQL

## Data Processing

* pandas
* openpyxl

## Visualization

* Plotly

## Frontend

* Streamlit for v0.1

## Deployment

* Docker
* Docker Compose

## Testing

* pytest
* FastAPI TestClient / httpx

## Code Quality

* ruff
* black
* mypy optional

## Future AI Integration

* OpenAI-compatible provider abstraction
* local model provider later
* auditable AI summaries

---

# Core Domain Entities

## Tenant

Represents an isolated workspace. In v0.1, this may be simplified or seeded as a default tenant.

## Company

Represents an organization participating in interoperability testing.

## Industry

Represents a business or operational domain such as logistics, healthcare, advertising, finance, manufacturing, energy, defense, or telecommunications.

## Capability

Represents what a company can provide or test within an industry.

Examples:

* Inventory Visibility
* Patient Data Exchange
* Campaign Analytics
* Secure Messaging
* Payment Processing

## System/Application

Represents the technical system used to support a capability.

Examples:

* SAP ERP
* SAP S/4HANA
* Oracle Database
* PostgreSQL
* REST API Gateway
* FHIR Server
* Kafka Service

## CompanyIndustry

Maps a company to an industry.

## IndustryCapability

Maps a capability to an industry context.

## CompanyCapabilitySnapshot

Represents the capabilities a company declares for a given year or project cycle.

This is important because companies change over time.

## Project

Represents the overall collaboration, mission, exercise, or testing program.

## ProjectCycle

Represents a specific year or cycle of a project.

Example:

* Supply Chain Exercise 2024
* Supply Chain Exercise 2025
* Supply Chain Exercise 2026

## Scenario

Represents an operational scenario.

Example:

A hospital requests emergency medical stock from a logistics provider.

## TestCase

Represents the external test case definition imported or referenced by CIIP.

## ImportBatch

Represents one uploaded CSV or Excel import.

## RawTestResult

Stores raw imported rows before normalization.

## NormalizedTestResult

Stores clean canonical test result records.

## GapTaxonomy

Represents common gap categories.

Examples:

* Data schema mismatch
* Authentication mismatch
* Missing API documentation
* Performance below SLA
* Terminology mismatch

## GapInstance

Represents a specific gap observed in a test result.

## ScoreSnapshot

Stores calculated score results for faster analytics.

## Report

Stores generated report metadata and content.

---

# Release Plan

## v0.1.0 — Interoperability Analytics MVP

Goal:

Build the first working local version.

Features:

* FastAPI backend
* PostgreSQL database
* Alembic migrations
* master data CRUD
* CSV/Excel import
* raw and normalized result storage
* basic scoring engine
* multi-year analytics
* capability coverage analytics
* partner diversity analytics
* persistent gap analytics
* Streamlit dashboard
* basic report generation
* synthetic demo dataset

Expected outcome:

A developer can run the full system locally with Docker Compose and demonstrate a multi-year interoperability analysis scenario using synthetic data.

## v0.2.0 — Improved Import and Data Quality

Goal:

Make imports more robust and user-friendly.

Features:

* import preview
* column mapping UI
* alias resolution
* duplicate detection
* rejected row management
* strict/permissive import modes
* improved validation reports
* import history
* data quality dashboard

## v0.3.0 — Advanced Analytics

Goal:

Improve analytical depth.

Features:

* year-over-year comparison
* persistent gap scoring
* repeated partner concentration index
* capability maturity trend
* industry-level maturity trend
* company profile analytics
* company pair drill-down
* project cycle comparison
* additional Plotly charts

## v0.4.0 — AI-Assisted Reporting

Goal:

Add controlled AI capabilities.

Features:

* LLM provider abstraction
* OpenAI-compatible provider
* structured analytics-to-summary prompts
* AI-generated executive summaries
* AI-generated next-year recommendations
* AI audit log
* prompt templates
* AI output review workflow

## v0.5.0 — API Connector Foundation

Goal:

Prepare for integration with external testing platforms.

Features:

* external platform connector abstraction
* mock connector
* scheduled import support
* connector configuration
* API-based result ingestion
* import job logs

## v0.6.0 — User and Role Model

Goal:

Add basic platform governance.

Features:

* local authentication
* users
* roles
* tenant admin
* analyst
* delegate
* viewer
* basic access rules
* audit events

## v0.7.0 — Reporting Enhancements

Goal:

Improve reporting outputs.

Features:

* report templates
* Markdown reports
* HTML reports
* PDF export
* report archive
* company-specific report generation
* project-cycle reports
* executive report view

## v0.8.0 — Evidence and Traceability

Goal:

Improve auditability.

Features:

* evidence URI management
* evidence metadata
* external evidence links
* evidence validation status
* test-result traceability view
* raw-to-normalized lineage

## v0.9.0 — Production Readiness Preparation

Goal:

Prepare for broader usage.

Features:

* stronger configuration management
* Docker production profile
* improved logging
* structured error responses
* performance optimization
* database indexing improvements
* API pagination
* API filtering
* OpenAPI documentation cleanup

## v1.0.0 — Stable Open-Source Release

Goal:

Release a stable open-source version.

Features:

* complete v0.x feature set
* clean documentation
* demo dataset
* deployment guide
* API documentation
* contributor guide
* test coverage target
* release notes
* license
* GitHub Actions CI
* stable migration history

---

# Development Phases for v0.1

## Phase 1 — Repository and Backend Foundation

Deliverables:

* repository scaffold
* Docker Compose
* FastAPI app
* PostgreSQL container
* health endpoint
* database connection check
* initial README

Status:

* In progress / partially completed

## Phase 2 — Alembic and Database Foundation

Deliverables:

* Alembic initialized
* SQLAlchemy Base
* migration setup
* first empty migration
* initial database versioning

## Phase 3 — Domain Models

Deliverables:

* SQLAlchemy models for core entities
* PostgreSQL enums
* relationships
* indexes
* first real schema migration

## Phase 4 — Seed Data

Deliverables:

* default interoperability layers
* default outcome values
* default gap taxonomy
* synthetic companies
* synthetic industries
* synthetic capabilities

## Phase 5 — Master Data APIs

Deliverables:

* company CRUD
* industry CRUD
* capability CRUD
* system CRUD
* project CRUD
* project cycle CRUD
* scenario CRUD
* test case CRUD

## Phase 6 — Import Pipeline

Deliverables:

* CSV upload
* Excel upload
* import batch creation
* raw row storage
* required column validation
* row-level validation
* import summary response

## Phase 7 — Normalization Pipeline

Deliverables:

* outcome normalization
* layer normalization
* company resolution
* industry resolution
* capability resolution
* system resolution
* normalized test result creation
* unresolved row handling

## Phase 8 — Scoring Engine

Deliverables:

* outcome-to-score logic
* pair score
* layer score
* industry score
* capability score
* year score
* score snapshot storage

## Phase 9 — Analytics Endpoints

Deliverables:

* overview KPIs
* pairwise matrix endpoint
* trend endpoint
* capability coverage endpoint
* partner diversity endpoint
* gap frequency endpoint
* persistent gap endpoint

## Phase 10 — Streamlit Dashboard

Deliverables:

* overview page
* import center page
* company analysis page
* capability coverage page
* gap analysis page

## Phase 11 — Reports

Deliverables:

* report data aggregation
* Markdown report generation
* HTML report generation
* report storage

## Phase 12 — Optional AI Summary

Deliverables:

* LLM provider interface
* structured analytics prompt
* executive summary generation
* AI summary audit log

---

# MVP Acceptance Criteria

CIIP v0.1 is considered complete when:

1. The project runs locally using Docker Compose.
2. FastAPI API is accessible.
3. PostgreSQL is running and migrated.
4. Master data can be created and listed.
5. A synthetic CSV/Excel external test result file can be imported.
6. Raw imported rows are preserved.
7. Normalized results are created.
8. Basic scores are calculated.
9. Multi-year analysis works for 2024, 2025, and 2026.
10. The system detects:

    * new capabilities
    * declared but untested capabilities
    * repeated partners
    * persistent gaps
11. Dashboard pages show core analytics.
12. A basic report can be generated.
13. Tests exist for core backend functions.
14. Documentation explains how to run the project.

---

# Suggested Branch Strategy

## Main Branches

```text
main
develop
```

## Supporting Branches

```text
feature/*
fix/*
docs/*
release/*
```

## Flow

```text
feature/* → develop → release/* → main
```

## Current Planned Branches

```text
feature/alembic-setup
feature/domain-models
feature/seed-data
feature/master-data-crud
feature/import-pipeline
feature/result-normalization
feature/scoring-engine
feature/analytics-endpoints
feature/streamlit-dashboard
feature/report-generation
feature/ai-summary
```

## Commit Message Style

Use simple conventional commits:

```text
feat: add Alembic setup
feat: add domain models
feat: add import pipeline
fix: correct Docker database port mapping
docs: add MVP and release plan
test: add scoring engine tests
refactor: reorganize analytics services
```

---

# Synthetic Demo Dataset Plan

The demo dataset should include:

## Companies

```text
Alpha Group
Beta Nexus
Gamma Works
```

## Industries

```text
Logistics
Healthcare
Advertising
```

## Years

```text
2024
2025
2026
```

## Demo Story

2024:

* Alpha Group tests logistics interoperability with Beta Nexus.
* Main capability: Inventory Visibility.
* Semantic gap appears.

2025:

* Alpha Group repeats logistics interoperability with Beta Nexus.
* Alpha Group adds healthcare interoperability with Gamma Works.
* Semantic gap partially remains.

2026:

* Alpha Group improves logistics interoperability.
* Alpha Group adds advertising interoperability with Gamma Works.
* Some declared capabilities are still untested.
* Partner concentration remains high with Beta Nexus.

## Demo Should Demonstrate

* year-over-year improvement
* repeated partner testing
* new capability addition
* persistent gap detection
* untested declared capability detection
* industry-level score comparison
* capability-level coverage analysis

---

# Documentation Plan

The `docs/` folder should contain:

```text
docs/
  architecture.md
  mvp-and-release-plan.md
  alembic-plan.md
  database-model.md
  api-design.md
  import-pipeline.md
  scoring-engine.md
  analytics-engine.md
  frontend-plan.md
  ai-integration-plan.md
```

Minimum documentation for v0.1:

```text
docs/
  architecture.md
  mvp-and-release-plan.md
  alembic-plan.md
  import-schema.md
  scoring-engine.md
```

---

# Immediate Next Steps

1. Fix Docker PostgreSQL port mapping if needed.

Correct mapping:

```yaml
ports:
  - "5434:5432"
```

2. Keep FastAPI Docker database URL as:

```env
DATABASE_URL=postgresql+psycopg://ciip_user:ciip_password@db:5432/ciip
```

3. Use local database URL for local Alembic or DBeaver:

```text
postgresql+psycopg://ciip_user:ciip_password@localhost:5434/ciip
```

4. Add and commit this document.

```bash
git add docs/mvp-and-release-plan.md
git commit -m "docs: add MVP and release plan"
git push
```

5. Continue with Alembic setup on `feature/alembic-setup`.

---

# License Recommendation

Use **Apache License 2.0** unless there is a strong reason to choose another license.

Reason:

* permissive
* business-friendly
* suitable for open-source infrastructure projects
* includes explicit patent grant
* widely accepted for enterprise and AI/data projects
