---
title: "Worklog Week 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:
* Study and practice configuring **Amazon CloudFront** to accelerate static content delivery for the Pet Resort & Care project.
* Draft, refine, and finalize the System Architecture Diagram based on S3 and CloudFront knowledge acquired in previous weeks.
* Review all data transit vectors on the blueprint, ensuring alignment with the AWS services studied in prior weeks.

### Tasks carried out this week:
| Day | Detailed Task | Start Date | Completion Date | Reference Material |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Research the fundamentals of **Amazon CloudFront**: Study CDN (Content Delivery Network), Edge Location, Distribution concepts and how CloudFront accelerates static content delivery for websites.<br>- Review AWS documentation on CloudFront use cases for static websites (Accelerate Static Websites). | 22/06/2026 | 22/06/2026 | Amazon CloudFront Documentation |
| 2 | - Practice creating a **CloudFront Distribution** on AWS Console: Point the Origin to the S3 Bucket `aws-first-cloud-journe...` created the previous week.<br>- Distribution created successfully with ID **E2NI0FJ3HELT9Z**, Status set to **Enabled** and currently in **Deploying** state. | 23/06/2026 | 24/06/2026 | FCJ Workshop - CloudFront Lab |
| 3 | - Analyze the physical directory boundaries of the local source code to map functional tiers (ReactJS Frontend, Spring Boot Backend, MySQL Database).<br>- Sketch the initial architecture blueprint on Draw.io, integrating the CloudFront + S3 flow into the diagram. | 25/06/2026 | 25/06/2026 | System Block Diagram |
| 4 | - Attend the office and browse the AWS Study Group community platforms to evaluate infrastructure blueprints from prior cohorts.<br>- Compile common architectural design pitfalls based on Admin review comments, cross-referencing with the team's CloudFront integration design. | 26/06/2026 | 26/06/2026 | AWS Study Group Community |
| 5 | - Execute structural updates to the diagram: explicitly isolate VPC boundaries, server placement across multiple Availability Zones, managed RDS MySQL layers, and the CloudFront Frontend distribution flow.<br>- Finalize the high-level group architecture blueprint and push updates to Hugo. | 27/06/2026 | 28/06/2026 | AWS Architecture Icon Set |

### Week 10 Achievements:

####  Mastered Amazon CloudFront Configuration for Static Websites
* **Understood CloudFront's Role in System Architecture:**
  * Learned that CloudFront is AWS's global CDN service that distributes static content (HTML, CSS, JS, images) from Edge Locations closest to end-users, significantly reducing access latency for the Pet Resort & Care project.
  * Understood the primary objective of this step: creating a **CloudFront Distribution** to deliver content stored in the S3 Bucket created in the previous week.
* **Successfully Practiced on AWS Console:**
  * On the CloudFront dashboard, a Distribution was successfully created with ID **E2NI0FJ3HELT9Z**.
  * The Origin of this distribution points to `aws-first-cloud-journe...` (the previously initialized S3 Bucket).
  * The Status has transitioned to **Enabled**, and the Last Modified status recorded the **Deploying** process completing successfully.

#### System Architecture Diagram Refinement & Blueprinting
* **Standardized Real-World Data Distribution Flows:**
  * Successfully visualized the application baseline flow: End-users querying domains via Route 53 -> Fetching static client structures from S3/CloudFront repositories -> Issuing RESTful API commands down to compute server hosts.
  * Distinctly separated network security boundaries (Network Isolation): positioning public entry nodes inside Public Subnets while encapsulating the active backend codebase and managed RDS MySQL layer deep inside Private Subnets.
* **Mitigated Systemic Logical Errors:**
  * Evaporated redundant or over-complicated architectural blocks (such as automated serverless Lambda functions or DynamoDB NoSQL nodes from the template) that do not match the team's native Spring Boot layout, avoiding potential questioning from project auditors.

####  Knowledge Synthesis from Expert Community Feedback
* Extensively reviewed active troubleshooting notes and comment feedbacks shared by AWS Study Group Admins on parallel infrastructure designs to refine the team's own layout.
* Mastered identification of critical charting flaws: inverted data flow vectors, exposing relational database targets to Public Subnets, or misconfiguring Security Groups firewall routing rules.
* Ensured structural compliance between theoretical cloud network layouts (S3, CloudFront) and the project's current local code repository.
