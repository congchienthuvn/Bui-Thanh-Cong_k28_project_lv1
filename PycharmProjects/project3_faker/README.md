# E-Commerce Fake Data Generator and PostgreSQ

This repository contains an automated Python data pipeline designed to generate synthetic e-commerce data and load it into a PostgreSQL database. The project incorporates production-grade database practices, including **Audit Columns** for tracking data lifecycle, **Soft Delete** functionality, constraints, and secure credential handling.

---

## Key Features

- **Large-Scale Synthetic Data Generation:** Utilizes the `Faker` library to generate realistic Vietnamese e-commerce entities (`Brand`, `Category`, `Seller`, `Customer`, `Product`, `Promotion`, and `Order`).
- **Enterprise-Standard Audit Columns:** All table schemas include dedicated audit metadata:
  - `created_at`, `created_by`: Record creation timestamp and author.
  - `updated_at`, `updated_by`: Last modification timestamp and user.
  - `is_deleted`, `deleted_at`, `deleted_by`: Flags and timestamps for soft-deletion handling.
- **Database Constraints and Integrity:** Enforces field checks directly at the database level (`price > 0`, `rating BETWEEN 0 AND 5`, discount bounds, and foreign key relationships).
- **Secure Configuration Management:** Separates database credentials from code using `database.ini` and prevents accidental exposure via `.gitignore`.

---

## Database Schema Overview

The system models a relational database schema with 9 core tables:

1. **`brand`**: Stores brand information and country of origin.
2. **`category`**: Supports hierarchical product classification (Parent and Child categories).
3. **`seller`**: Manages seller types (Official vs. Marketplace) and store ratings.
4. **`customer`**: Stores customer profiles, locations, and contact details.
5. **`product`**: Tracks inventory, pricing, ratings, and operational status.
6. **`promotion`**: Defines promotional campaigns (Percentage-based or fixed-amount discounts).
7. **`promotion_product`**: Mapping table linking products to promotional events.
8. **`order`**: Manages customer order headers and statuses (`PLACED`, `PAID`, `SHIPPED`, `DELIVERED`, `CANCELLED`, `RETURNED`).
9. **`order_item`**: Stores transactional line items and calculated subtotals.

---

## Project Structure

```text
project3_faker/
├── config.py         # Parses connection strings from database.ini
├── database.ini      # Local PostgreSQL credential storage (Excluded from VCS)
├── models.py         # DDL table definition queries in Python
├── generators.py     # Data generation logic using Faker
├── loader.py         # Database initialization and bulk insert loader using psycopg3
├── main.py           # Main execution entry point
├── pyproject.toml    # Dependency configuration file
└── README.md         # Project documentation