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

## 🗂️ Repository Structure

---

## 📖 Curriculum Sections

### 🟢 Section 1: Introduction to Django ORM
**Duration:** 2 Weeks | **Status:** ✅ Completed

#### Topics Covered:
- Setting up Django project with database configuration
- Understanding the Model-View-Template (MVT) architecture
- Creating your first Django models
- Django migration system basics
- SQLite vs PostgreSQL vs MySQL in Django
- Database connection settings and environment variables

#### Key Learnings:
```python
# Example: Basic Model Definition
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

Category Technologies
Backend Django 4.2+, Django REST Framework
Databases PostgreSQL, MySQL, SQLite
Caching Redis, Memcached
Testing pytest, Django TestCase
Monitoring Django Debug Toolbar, Prometheus
CI/CD GitHub Actions, Docker, Kubernetes
