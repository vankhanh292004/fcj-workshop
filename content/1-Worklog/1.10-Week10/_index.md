---
title: "Worklog Week 10"
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:
* Focus on analyzing, drafting, and refining the System Architecture Diagram for the Pet Resort & Care project.
* Research and reference architecture evaluation threads and admin comments within the AWS Study Group community to optimize the design.
* Review all data transit vectors on the blueprint, ensuring alignment with the simplified infrastructure directions studied in Weeks 8 and 9.

### Tasks carried out this week:
| Day | Detailed Task | Start Date | Completion Date | Reference Material |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Analyze the physical directory boundaries of the local source code to map functional tiers (ReactJS Frontend, Spring Boot Backend, MySQL Database).<br>- Sketch the initial blueprint on Draw.io. | 22/06/2026 | 22/06/2026 | System Block Diagram |
| 2 | - Attend the office and browse the AWS Study Group community platforms to evaluate infrastructure blueprints from prior cohorts.<br>- Compile common architectural design pitfalls based on Admin review comments. | 23/06/2026 | 23/06/2026 | AWS Study Group Community |
| 3 | - Cross-reference the team's blueprint with the actual codebase; inspect if connection flows are over-engineered or include unutilized services.<br>- Verify the technical logic of API routing arrows. | 24/06/2026 | 24/06/2026 | |
| 4 | - Execute structural updates to the diagram: explicitly isolate the Amazon VPC boundaries, server placement across multiple Availability Zones, and managed RDS MySQL layers to align with the High Availability architecture direction. | 25/06/2026 | 25/06/2026 | AWS Architecture Icon Set |
| 5 | - Finalize the formal high-level group system architecture blueprint.<br>- Author brief functional logs detailing data interaction paths, review the complete registry layout, and push updates to Hugo. | 26/06/2026 | 26/06/2026 | |

### Week 10 Achievements:

#### A. System Architecture Diagram Refinement & Blueprinting
* **Standardized Real-World Data Distribution Flows:**
  * Successfully visualized the application baseline flow: End-users querying domains via Route 53 -> fetching static client structures from S3/CloudFront repositories -> issuing RESTful API commands down to compute server hosts.
  * Distinctly separated network security boundaries (Network Isolation): positioning public entry nodes inside Public Subnets while encapsulating the active backend codebase and managed RDS MySQL layer deep inside Private Subnets.
* **Mitigated Systemic Logical Errors:**
  * Evaporated redundant or over-complicated architectural blocks (such as automated serverless Lambda functions or DynamoDB NoSQL nodes from the template) that do not match the team's native Spring Boot layout, avoiding potential questioning from project auditors.

#### B. Knowledge Synthesis from Expert Community Feedback
* **Studied Real-World Infrastructure Assessments:**
  * Extensively reviewed active troubleshooting notes and comment feedbacks shared by AWS Study Group Admins on parallel infrastructure designs to refine our own layout.
  * Mastered identification of critical charting flaws: inverted data flow vectors, exposing relational database targets to Public Subnets, or misconfiguring Security Groups firewall routing rules.

#### C. Operational Code and Cloud Infrastructure Alignment
* Ensured structural compliance between theoretical cloud network layouts and the project's current local code repository.
* Upheld a highly realistic and minimal design philosophy, focusing strictly on populating pet media/invoice storage via S3 and securing stable execution environments for Spring Boot, allowing the team to retain absolute control over the platform footprint without knowledge overload.
