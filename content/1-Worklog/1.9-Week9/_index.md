---
title: "Worklog Week 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

- Optimize source code security configurations and local database query efficiency for the Pet Resort & Care project.
- Investigate theoretical concepts surrounding monitoring and logging tools available on the AWS platform.
- Conduct extensive testing of edge-case scenarios in the local environment to prepare for broader application delivery.

### Tasks carried out this week:

| Day | Detailed Task                                                                                                                                                                                                                                                     | Start Date | Completion Date | Reference Material          |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | --------------------------- |
| 1   | - Audit backend layer workflows within `ProductServiceImpl` and `BookingServiceImpl`.<br>- Inspect and optimize JPA/Hibernate query methodologies regarding orders and reservations to mitigate N+1 query bottlenecks.                                            | 15/06/2026 | 15/06/2026      | Spring Data JPA Guide       |
| 2   | - Review foundational concepts of managed cloud monitoring via **Amazon CloudWatch**.<br>- Study baseline components: CloudWatch Metrics (CPU Utilization, Network In/Out), Log Groups, and CloudWatch Alarms execution behaviors.                                | 16/06/2026 | 16/06/2026      | Amazon CloudWatch Docs      |
| 3   | - Harden the local `application.yml` layout by decoupling sensitive configurations (Database connection URL, Username, Password, and JWT Secret Keys) away from plain text code parameters.<br>- Migrate variables into system-level Environment Variables.       | 17/06/2026 | 17/06/2026      | AWS Security Best Practices |
| 4   | - Study the architecture of **Amazon CloudWatch Dashboards** for monitoring EC2 instances and Application Load Balancers.<br>- Learn how to create custom dashboards combining CPU, Memory, Network metrics and ALB Health Check statuses for future system administration.                   | 18/06/2026 | 18/06/2026      | AWS CloudWatch Dashboard Docs |
| 5   | - Utilize Postman utilities to run local error scenario simulations: issuing expired JWT bearer tokens and pushing invalid payload attributes to booking endpoints.<br>- Refine the centralized `GlobalExceptionHandler` filter layer and update Hugo registries. | 19/06/2026 | 19/06/2026      | Guide to API Error Handling |

### Week 9 Achievements:

- **Local Infrastructure Performance Tuning:**
  - Successfully optimized relationship fetching configurations (FetchType properties) within persistent JPA entities (such as `Order` and `Booking` models), decreasing redundant database connection lookups.
  - Enforced asset credential obfuscation: removed hardcoded database passwords and security keys from file directories, shifting configurations to dynamic runtime loads to guarantee asset safety on GitHub repositories.

- **Acquired Infrastructure Observability Fundamentals (Monitoring & Cloud Logging):**
  - Conceptualized how **Amazon CloudWatch** polls real-time host compute capacity logs, allowing cloud administrators to evaluate scaling actions on underlying EC2 runtime hosts.
  - Mastered the baseline logic of centralizing application operation logs (Log Groups framework), which acts as a crucial asset for trace execution analysis and debugging sequences once deployed to cloud networks.

- **Validated Robust System Fault-Tolerance & Exception Handling:**
  - Upgraded the global error catch filter `GlobalExceptionHandler`: guaranteed all technical failures (invalid syntax structure, request payload formatting, missing indices, or custom `ResourceNotFoundException` entries) map neatly back to unified JSON response wrappers (`ApiResponse`).
  - Verified backend system endurance via rigorous local Postman tests with anomalous runtime parameters, ensuring host processes remain resilient against corrupted external queries.

- **Streamlined Environment Variables Mapping Documentation:**
  - Documented the complete directory list of systemic variables required to seamlessly map identical execution environments onto the AWS Web Console in upcoming phases.
