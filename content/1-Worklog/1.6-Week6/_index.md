---
title: "Worklog Week 6"
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:
* Attend the office for self-study sessions and group discussions to resolve outstanding cloud infrastructure queries.
* Review, audit, and systematize knowledge regarding the core service groups covered (IAM, S3, VPC, EC2).
* Investigate theoretical static hosting solutions and draft the preliminary architecture diagram for the Pet Resort & Care project.

### Tasks carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | Attend the office for self-study; audit and review all AWS account security configurations (Root Account & IAM Users), and optimize Password Policies. | 25/05/2026 | 25/05/2026 | AWS IAM Documentation |
| 2 | Conduct a deep-dive review into Amazon S3 storage services; practice advanced security setups including S3 Block Public Access and Object Ownership. | 26/05/2026 | 26/05/2026 | Amazon S3 Guide |
| 3 | Participate in office group discussions; re-examine VPC subnetting theories, inbound/outbound traffic flows through Public/Private Subnets, and Security Groups configurations. | 27/05/2026 | 27/05/2026 | Amazon VPC Documentation |
| 4 | Study theoretical implementations for distributing static frontends; explore how to combine Amazon S3 with Amazon CloudFront (CDN) to optimize page loading speeds. | 28/05/2026 | 28/05/2026 | AWS Web Hosting Blog |
| 5 | Practice drafting the preliminary system architecture for the Pet Resort & Care project using Draw.io; compile documentation for the upcoming Proposal week. | 29/05/2026 | 29/05/2026 | |

### Week 6 Achievements:

* **Comprehensive Core Knowledge Systematization:** Mastered the operational mechanics of core AWS service branches (Compute, Networking, Storage, Security) mid-internship, ensuring a solid foundation before major deployment phases.

* **Optimized Internship Account Security:**
  * Verified successful Multi-Factor Authentication (MFA) activation for both Root and IAM User accounts.
  * Implemented the Principle of Least Privilege across member IAM Users to enforce strict resource governance.

* **Proficiency in AWS CLI Core Operations for Resource Auditing:**
  * `aws sts get-caller-identity`: Verified and authenticated the current active IAM User identity.
  * `aws s3 ls`: Listed running storage cluster repositories (S3 Buckets) within the environment.
  * Practiced command-line asset bucket provisioning and termination sequences to adapt to terminal-based resource management.

* **Refined Secure Network Architecture Design Thinking:** Understood how to position an Application Load Balancer (ALB) in Public Subnets to face internet entry points while shielding core resources (EC2 Spring Boot Backend, RDS MySQL) inside Private Subnets away from public exposure.

* **Completed the Draft Architecture Diagram:** Formulated a distinct roadmap for the Pet Shop layout, tracing user requests from Route 53, fetching static UI components from CloudFront/S3 Frontend, up to API routing towards the backend layer.

* **Enhanced Independent Study and Peer Collaboration:** Resolved remaining hands-on lab blocks through direct interaction and knowledge sharing with team members during office hours.