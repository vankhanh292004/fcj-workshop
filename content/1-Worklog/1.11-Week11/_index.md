---
title: "Worklog Week 11"
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Core Objectives
- Review the overall project topology design for the Pet Resort network infrastructure.
- Implement a VPC Endpoint (S3 Gateway Endpoint) to optimize internal data transmission paths.
- Reduce NAT Gateway billing costs by enabling private EC2 instances to download S3 assets without accessing the public Internet.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Consolidate the active network topology diagram and cross-reference with launched AWS resources. | 26/06/2026 | 26/06/2026 | |
| 2 | Analyze AWS Billing reports, identifying high NAT Gateway data processing fees due to image transfers from S3 to EC2. | 27/06/2026 | 27/06/2026 | |
| 3 | Study AWS VPC Endpoints types (Gateway vs Interface Endpoints). | 29/06/2026 | 29/06/2026 | [VPC Endpoints Docs](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) |
| 4 | Create an Amazon S3 Gateway Endpoint and associate it with the Route Tables of Private Subnets. | 30/06/2026 | 30/06/2026 | [S3 Gateway Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) |
| 5 | Modify S3 Bucket Policies and Security Groups to permit internal endpoint access. | 01/07/2026 | 01/07/2026 | |
| 6 | Perform download benchmarks from EC2 in the Private Subnet to verify that data travels strictly through the VPC endpoint. | 02/07/2026 | 02/07/2026 | |

### Achievements
- Optimized data transport pathways between Amazon EC2 and Amazon S3.
- Significantly reduced NAT Gateway processing fees by routing S3 traffic internally within the AWS private fiber network.
- Standardized and updated the final network topology diagram for report documentation.