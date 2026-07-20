---
title: "Worklog Week 7"
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Core Objectives
- Launch Amazon EC2 virtual servers isolated within Private Subnets.
- Configure Linux compute environments (Amazon Linux or Ubuntu).
- Install Java Runtime Environments (JRE/JDK) and prepare systems to host the Spring Boot backend.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Analyze EC2 Instance Types and select optimal sizing (`t3.medium` or `t3.micro`) suitable for Spring Boot apps. | 29/05/2026 | 29/05/2026 | [Amazon EC2 Docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) |
| 2 | Launch Amazon Linux 2 EC2 instances within Private Subnets across different AZs. | 30/05/2026 | 30/05/2026 | |
| 3 | Generate and securely manage SSH Key Pairs (.pem keys) for administrative console access. | 01/06/2026 | 01/06/2026 | |
| 4 | Deploy a Bastion Host (or EC2 Instance Connect Endpoint) to bridge SSH connections into the Private Subnet. | 02/06/2026 | 02/06/2026 | |
| 5 | Establish SSH session to the EC2 host and install OpenJDK 17 alongside system packages. | 03/06/2026 | 03/06/2026 | |
| 6 | Package the Spring Boot backend locally and transfer the executable `.jar` file to EC2 to verify environment startup. | 04/06/2026 | 04/06/2026 | |

### Achievements
- Successfully provisioned secure EC2 instances nested within Private Subnets.
- Installed Java 17 runtimes on the EC2 instances, ready for production backend execution.
- Established a secure administration bridge using a Bastion Host, maintaining secure boundary access controls.