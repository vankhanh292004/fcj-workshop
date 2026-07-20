---
title: "Worklog Week 3"
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Core Objectives
- Design the core network topology on AWS using Amazon VPC.
- Allocate CIDR Blocks and configure appropriate Subnet ranges for the Pet Care system.
- Establish clear boundaries between internal networks (Private Subnets) for Databases/Backends and public networks (Public Subnets) for Load Balancers/NAT.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Study VPC architecture, CIDR block allocation, and IP planning strategies. | 01/05/2026 | 01/05/2026 | [Amazon VPC Docs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) |
| 2 | Draft VPC design schemas containing 2 Availability Zones (AZs) to ensure high availability. | 02/05/2026 | 02/05/2026 | |
| 3 | Create the primary project VPC with CIDR `10.0.0.0/16` on the AWS Management Console. | 04/05/2026 | 04/05/2026 | |
| 4 | Configure 2 Public Subnets (one per AZ) to receive incoming traffic from the Internet. | 05/05/2026 | 05/05/2026 | |
| 5 | Configure 4 Private Subnets (2 for Backend App, 2 for RDS Database) to isolate sensitive resources. | 06/05/2026 | 06/05/2026 | |
| 6 | Validate IP allocation sheets for the VPC and finalize the core network layout. | 07/05/2026 | 07/05/2026 | |

### Achievements
- Successfully created a stable Amazon VPC as the core networking foundation for the project.
- Configured 2 Public Subnets and 4 Private Subnets spanned across 2 Availability Zones.
- Ensured network-level isolation for system resources.