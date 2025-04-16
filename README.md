## Design and Administration of Databases
This is a repository for my DABD(Design and Administration of Databases) course. I only upload the more interesting laboratory sessions.

### Lab6
---
### 🧰 Project Overview

It consists of building a web server using Django and an ORM (Object Relational Mapping) system to manage products, variants, and categories.

You will:

- Set up a Django web server with an admin interface.
- Define models for:
  - Product templates (ProductTemplate)
  - Product variants (ProductVariant)
  - Product categories (ProductCategory)
- Build a simple frontend with custom views and URLs.
- Generate test data using the Faker and Random libraries.

### 🚀 Getting Started

#### 1. Set up a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install Django==5.2 Faker
