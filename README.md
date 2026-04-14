#  Intelligent Systems QA Framework

> Enterprise-grade Test Automation Framework for Intelligent Systems
> Built with Python, Playwright, pytest and GitHub Actions CI/CD

![CI/CD Pipeline](https://github.com/YOUR_USERNAME/intelligent_systems_qa/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.44-green)
![pytest](https://img.shields.io/badge/pytest-7.4-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 👤 About the Author

**Senior QA Lead | 14+ Years Experience**
- 🎯 Specialization: Big Data QA, Distributed Systems, AI/ML Testing
- 🏢 Target Domain: Intelligent Systems, Data Platforms, AI Infrastructure
- 🔗 LinkedIn: [https://www.linkedin.com/in/alaka-pattnaik/]
- 📧 Email: alakap2026@gmail.com

---

## 🎯 Project Overview

This framework demonstrates enterprise-level test automation 
capabilities for intelligent systems — covering UI automation, 
REST API validation, and a scalable architecture designed to 
grow into AI/ML model testing and Big Data pipeline validation.

### Why this framework?


### Test Tiering Overview
    Tier 1 = highest priority:  Business‑Critical (Runs hourly + on push)

    Tier 2 = mid‑priority:  Supporting (Runs on PRs)

    Tier 3 = low‑risk:  Low‑Risk (Runs daily)
                ┌──────────────────────────┐
                │        🟢 TIER 1         │
                │   Business‑Critical      │
                │  • Login UI tests        │
                │  • Create/Get User API   │
                │                          │
                │ Runs: Hourly + On Push   │
                └─────────────▲────────────┘
                              │
                              │
                ┌─────────────┴────────────┐
                │        🟡 TIER 2         │
                │     Supporting Tests      │
                │  • Username/Password UI   │
                │  • Update/Delete User API │
                │                           │
                │ Runs: Pull Requests       │
                └─────────────▲────────────┘
                              │
                              │
                ┌─────────────┴────────────┐
                │        🔵 TIER 3         │
                │   Stable / Low‑Risk       │
                │  • Remember Me UI         │
                │  • List Users API         │
                │                           │
                │ Runs: Daily Schedule      │
                └──────────────────────────┘
