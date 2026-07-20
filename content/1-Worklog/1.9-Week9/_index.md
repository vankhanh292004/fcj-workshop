---
title: "Worklog Week 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Core Objectives
- Migrate the relational MySQL database to managed Amazon RDS with Multi-AZ high-availability enabled.
- Provision an Amazon ElastiCache (Redis) cluster to optimize performance and handle user shopping cart operations smoothly.
- Define secure network access paths for both the database and the cache layer.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Research Amazon RDS Multi-AZ architecture and Redis caching benefits on AWS infrastructure. | 12/06/2026 | 12/06/2026 | [Amazon RDS Docs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) |
| 2 | Create a DB Subnet Group using Private Subnets dedicated to the RDS database instances. | 13/06/2026 | 13/06/2026 | |
| 3 | Launch an RDS MySQL instance with Multi-AZ configuration to support automatic failover across Availability Zones. | 15/06/2026 | 15/06/2026 | |
| 4 | Provision an Amazon ElastiCache (Redis) cluster in the designated database Private Subnets. | 16/06/2026 | 16/06/2026 | [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) |
| 5 | Configure Security Groups to allow inbound TCP connections from Backend EC2 instances to port `3306` (MySQL) and `6379` (Redis). | 17/06/2026 | 17/06/2026 | |
| 6 | Populate the database schema onto the RDS instance and verify connectivity using a secure database client via Bastion tunnel. | 18/06/2026 | 18/06/2026 | |

### Achievements
- Successfully migrated MySQL database to a highly available Amazon RDS Multi-AZ setup with automated failover.
- Configured ElastiCache Redis for fast in-memory shopping cart caching.
- Isolated database and caching tiers from public internet exposure by routing traffic solely through backend services.
