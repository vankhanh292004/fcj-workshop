---
title: "Worklog Week 4"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Core Objectives
- Set up network gateways to connect the VPC to external resources (Internet Gateway & NAT Gateway).
- Configure Route Tables to direct packet traffic for each subnet type (Public & Private).
- Create and configure instance-level firewalls (Security Groups) to regulate inbound and outbound data streams.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Create an Internet Gateway (IGW) and attach it to the project VPC to enable Internet access for Public Subnets. | 08/05/2026 | 08/05/2026 | [VPC Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) |
| 2 | Configure Route Tables for Public Subnets to direct `0.0.0.0/0` traffic through the Internet Gateway. | 09/05/2026 | 09/05/2026 | |
| 3 | Allocate an Elastic IP and launch a NAT Gateway in the Public Subnet to allow one-way outbound Internet access for Private Subnets. | 11/05/2026 | 11/05/2026 | [NAT Gateway Docs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) |
| 4 | Update Route Tables for Private Subnets to forward outgoing Internet-bound traffic through the NAT Gateway. | 12/05/2026 | 12/05/2026 | |
| 5 | Design specific Security Groups for the Application Load Balancer, EC2 Web Servers, and RDS Database. | 13/05/2026 | 13/05/2026 | [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) |
| 6 | Set up Inbound/Outbound rules (e.g., restrict EC2 to ALB traffic only, restrict RDS to EC2 traffic only). | 14/05/2026 | 14/05/2026 | |

### Achievements
- Completed VPC network routing: Public Subnets communicate bidirectionally with the Internet, while Private Subnets maintain secure outbound-only connection through the NAT Gateway.
- Established fine-grained Security Group rules, ensuring unauthorized external connections cannot bypass intermediate tiers to reach the Backend or Database.