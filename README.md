# 📚 ALX Django Database Learning Path

[![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![SQLite](https://img.shields.io/badge/-SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/-GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)](https://github.com/features/actions)

## 🎯 Learning Path Overview

This repository contains my comprehensive journey through ALX's Django Database curriculum. The learning path covers everything from fundamental ORM concepts to advanced database optimization techniques in Django applications.

---

---

## 🧪 Database Local Test

### Quick Database Connection Test

To verify your database setup is working correctly, run the database test script:

```bash
# Navigate to the repository root
cd alx-django-database

# Run the database test script
python scripts/test_db_connection.py

## Test Output Examples
🚀 Starting Database Connection Test...
==================================================

✅ Testing SQLite Connection...
   - Database path: db.sqlite3
   - Connection successful!
   - Version: 3.36.0

✅ Testing PostgreSQL Connection...
   - Host: localhost
   - Port: 5432
   - Database: django_db
   - Connection successful!
   - Version: PostgreSQL 14.5

✅ Testing MySQL Connection...
   - Host: localhost
   - Port: 3306
   - Database: django_db
   - Connection successful!
   - Version: MySQL 8.0.31

==================================================
📊 Test Results Summary:
   ✅ SQLite: PASSED
   ✅ PostgreSQL: PASSED
   ✅ MySQL: PASSED

🎉 All database connections are working!
