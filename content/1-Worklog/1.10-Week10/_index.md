---
title: "Worklog Week 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Core Objectives
- Configure real-time infrastructure monitoring using Amazon CloudWatch.
- Collect and analyze CPU, RAM, Network usage metrics of EC2 and database connection metrics of RDS.
- Build an automated notifications pipeline using Amazon Simple Notification Service (SNS) to alert administrators when alarms trigger.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Study Amazon CloudWatch services (Metrics, Alarms, Logs) and Amazon SNS subscription mechanisms. | 19/06/2026 | 19/06/2026 | [Amazon CloudWatch Docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) |
| 2 | Install and configure CloudWatch Agent on EC2 hosts to stream system and Spring Boot logs to CloudWatch Log Groups. | 20/06/2026 | 20/06/2026 | |
| 3 | Create an Amazon SNS Topic named `system-alerts` and configure email subscriptions. | 22/06/2026 | 22/06/2026 | [Amazon SNS Docs](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) |
| 4 | Setup CloudWatch Alarms to monitor average EC2 CPU Utilization (triggering when CPU > 80% for 5 consecutive minutes). | 23/06/2026 | 23/06/2026 | |
| 5 | Configure CloudWatch Alarms for RDS Database Connections and HTTP 5XX response counts on the Application Load Balancer. | 24/06/2026 | 24/06/2026 | |
| 6 | Simulate high CPU utilization on EC2 to trigger Alarms and verify email notification delivery via SNS. | 25/06/2026 | 25/06/2026 | |

### Achievements
- Successfully integrated centralized CloudWatch logging and metrics dashboard for infrastructure tracking.
- Set up flexible performance alarm thresholds to proactively detect system degradation.
- Established automated notification paths via email through Amazon SNS for quick operation team response.
