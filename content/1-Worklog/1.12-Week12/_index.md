---
title: "Worklog Week 12"
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Core Objectives
- Integrate and establish connectivity across the 3-Tier services: ReactJS Frontend, Spring Boot Backend, and RDS Database.
- Launch the integrated web application onto the public Internet via CloudFront CDN and ALB endpoints.
- Configure CORS controls, database transaction configurations, and end-to-end integration pathways.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Map database credentials (JDBC URL, RDS endpoint, credentials) into the Spring Boot backend configuration files (`application.properties`). | 03/07/2026 | 03/07/2026 | |
| 2 | Start backend services on EC2 instances inside Private Subnets and verify database connection logs. | 04/07/2026 | 04/07/2026 | |
| 3 | Recompile the ReactJS Frontend assets, redirecting the API Endpoint configuration to resolve to the ALB Domain name/URL. | 06/07/2026 | 06/07/2026 | |
| 4 | Configure CORS (Cross-Origin Resource Sharing) headers in the Spring Boot application to accept requests from the CloudFront distribution. | 07/07/2026 | 07/07/2026 | |
| 5 | Upload the updated ReactJS frontend build to the S3 bucket and trigger a cache Invalidation on the CloudFront Distribution. | 08/07/2026 | 08/07/2026 | [CloudFront Invalidation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) |
| 6 | Access the website via CloudFront domain, testing user registration, spa bookings, and transaction flows to verify end-to-end functionality. | 09/07/2026 | 09/07/2026 | |

### Achievements
- Successfully integrated and unified the 3-tier architecture (Frontend - Backend - Database) components.
- Launched the application on the public Internet using CloudFront CDN and ALB.
- Verified that all core features (registration, spa scheduling, shopping cart) execute properly end-to-end.