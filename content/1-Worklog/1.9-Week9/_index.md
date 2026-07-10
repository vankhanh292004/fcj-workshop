---
title: "Worklog Week 9"
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

- Study the **Amazon S3** object storage service and practice initializing S3 Buckets for storing pet images and invoices in the Pet Resort & Care project.
- Optimize backend source code security configurations and local database query performance.
- Research S3 Bucket naming conventions, object ownership management, and access policies on Amazon S3.

### Tasks carried out this week:

| Day | Detailed Task                                                                                                                                                                                                                                                     | Start Date | Completion Date | Reference Material          |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------- | --------------------------- |
| 1   | - Audit backend layer workflows within `ProductServiceImpl` and `BookingServiceImpl`.<br>- Inspect and optimize JPA/Hibernate query methodologies regarding orders and reservations to mitigate N+1 query bottlenecks.                                            | 15/06/2026 | 15/06/2026      | Spring Data JPA Guide       |
| 2   | - Research the fundamentals of **Amazon S3** (Simple Storage Service): Study core concepts including Buckets, Objects, Keys, and common use cases (static hosting, data backup, content distribution).<br>- Review AWS documentation on S3 Bucket naming rules (must be globally unique). | 16/06/2026 | 16/06/2026      | Amazon S3 Documentation     |
| 3   | - Practice creating an S3 Bucket on AWS Console: Enter the name `aws-first-cloud-journey`, set the Region to **Asia Pacific - Singapore (ap-southeast-1)**.<br>- Configure Object Ownership to **ACLs disabled** as recommended by AWS. Handle bucket name collision errors by appending numeric suffixes to ensure global uniqueness. | 17/06/2026 | 18/06/2026      | FCJ Workshop - S3 Lab       |
| 4   | - Harden the local `application.yml` layout by decoupling sensitive configurations (Database connection URL, Username, Password, and JWT Secret Keys) away from plain text code parameters.<br>- Migrate variables into system-level Environment Variables.       | 19/06/2026 | 19/06/2026      | AWS Security Best Practices |
| 5   | - Utilize Postman to run local error scenario simulations: issuing expired JWT bearer tokens and pushing invalid payload attributes to booking endpoints.<br>- Refine the centralized `GlobalExceptionHandler` filter layer and push updates to the Hugo site.     | 20/06/2026 | 21/06/2026      | Guide to API Error Handling |

### Week 9 Achievements:

- **Mastered Amazon S3 Fundamentals (S3 Bucket Initialization & Naming Rules):**
  - Gained a thorough understanding of Amazon S3 as a virtually limitless object storage service, perfectly suited for storing pet images, invoices, and static assets for the Pet Resort & Care project.
  - Successfully completed the S3 Bucket creation workflow on AWS Console: Entered the name `aws-first-cloud-journey`, configured the region to **ap-southeast-1 (Singapore)**, and set **Object Ownership** to **ACLs disabled** in compliance with AWS security best practices.
  - Documented a key lesson: S3 Bucket names must be **globally unique**. When a duplicate name is entered, the system displays a red error message *"Bucket with the same name already exists"*, requiring users to append numeric suffixes to avoid collisions.

- **Local Infrastructure Performance Tuning:**
  - Successfully optimized relationship fetching configurations (FetchType properties) within persistent JPA entities (such as `Order` and `Booking` models), significantly decreasing redundant database connection lookups.
  - Enforced asset credential obfuscation: removed hardcoded database passwords and security keys from configuration files, shifting configurations to dynamic runtime loads via system Environment Variables.

- **Validated Robust System Fault-Tolerance & Exception Handling:**
  - Upgraded the global error catch filter `GlobalExceptionHandler`: guaranteed all technical failures (invalid syntax structure, request payload formatting, missing indices, or custom `ResourceNotFoundException` entries) map neatly back to unified JSON response wrappers (`ApiResponse`).
  - Verified backend system endurance via rigorous local Postman tests with anomalous runtime parameters, ensuring host processes remain resilient against corrupted external queries.

- **Streamlined Infrastructure Documentation:**
  - Documented the complete directory of required environment variables alongside S3 configuration details, preparing for seamless integration onto the AWS platform in upcoming phases.
