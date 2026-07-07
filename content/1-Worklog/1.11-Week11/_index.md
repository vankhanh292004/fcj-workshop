---
title: "Worklog Week 11"
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

* Receive feedback from Admins/Mentors to revise, optimize, and finalize the final AWS architecture diagram.
* Deploy the entire Pet Resort & Care System project (both Frontend and Backend) to the actual Cloud environment based on the finalized architecture.
* Ensure the system operates stably on the 3-Tier architecture, meeting High Availability (Multi-AZ) and closed security requirements.

### Tasks to be implemented this week:
| Day | Task | Start Date | End Date | References |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| Monday | - Receive feedback from admin: Fix the CloudFront flow for distributing Frontend and Media content to avoid flow errors; redraw connection lines for visual clarity.<br>- Finalize the AWS architecture blueprint. | 29/06/2026   | 29/06/2026      | Feedback from AWS Study Group Admin       |
| Tuesday | - Deploy Network & Security Layer: Initialize VPC, Public/Private Subnets (Multi-AZ), NAT Gateway.<br>- Set up Security Groups, IAM Roles, KMS, and Secrets Manager.                            | 30/06/2026   | 30/06/2026      | AWS Documentation (VPC, IAM, KMS)         |
| Wednesday | - Deploy Data Tier: Install Amazon RDS MySQL (Multi-AZ, Sync Replication) and Amazon ElastiCache (Redis) using the Cache-Aside model.                                         | 01/07/2026   | 01/07/2026      | AWS Documentation (RDS, ElastiCache)      |
| Thursday | - Deploy Compute Tier: Push Spring Boot Backend source code to EC2.<br>- Configure Auto Scaling Group and manage traffic with Application Load Balancer (ALB).            | 02/07/2026   | 03/07/2026      | AWS Documentation (EC2, ALB, Auto Scaling)|
| Saturday | - Deploy Edge Layer: Upload ReactJS static source code to S3 Frontend, create S3 Media.<br>- Configure CloudFront to route requests and attach AWS WAF to protect the system.        | 04/07/2026   | 04/07/2026      | AWS Documentation (CloudFront, S3, WAF)   |

### Achievements in Week 11:

#### A. Architecture Finalization
* Successfully fixed logic errors in the Data Flow design based on Admin's feedback: Clearly separated the role of CloudFront combined with S3 for the static Frontend, and the direct Media resource retrieval flow.
* Finalized a professional 3-Tier architecture diagram, fully prepared for the final project reporting and acceptance phase.

#### B. Cloud Deployment
* Successfully migrated the entire *Pet Resort & Care System* from the Local environment to the actual AWS infrastructure.
* The system is now accessible smoothly via the Internet using a custom domain. API calls from Frontend to Backend, as well as image/media retrieval flows, operate seamlessly through the global CDN.
* Successfully applied Zero Trust security principles: Completely disabled SSH port (Port 22), isolated the Database within the Private Subnet, and securely managed credentials using AWS Secrets Manager.

#### C. Deployment Evidence

* **VPC Resource Map:** Visualizing the subnet structure, route tables, and gateways for the Multi-AZ setup.
  ![VPC Resource Map](/images/1-Worklog/vpc_resource_map.png)

* **Security Groups:** Structured firewall rules configured for ALB, Backend, Database, and Cache.
  ![Security Groups](/images/1-Worklog/security_groups.png)

* **RDS Database Initialization & Pricing:** Database estimated monthly cost details during RDS MySQL configuration.
  ![RDS Database Estimated Costs](/images/1-Worklog/rds_estimated_costs.png)

* **RDS MySQL Instance Launch:** The `petshop-database-1` instance in `Creating` status.
  ![RDS Instance Launching](/images/1-Worklog/rds_creating.png)

* **RDS Connectivity & Details:** Database specifications showing its private endpoint and Multi-AZ ready placement.
  ![RDS Connectivity Details](/images/1-Worklog/rds_connectivity.png)