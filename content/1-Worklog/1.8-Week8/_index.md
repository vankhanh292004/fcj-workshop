---
title: "Worklog Week 8"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Core Objectives
- Construct a traffic routing mechanism using Application Load Balancers (ALB) in Public Subnets.
- Configure target groups to direct HTTP/HTTPS requests to Spring Boot EC2 instances.
- Define Auto Scaling Groups (ASG) and scaling policies to dynamically launch/terminate instances based on real-time application load.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Research Elastic Load Balancing (ELB) mechanisms and Auto Scaling patterns. | 05/06/2026 | 05/06/2026 | [AWS ALB Docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) |
| 2 | Create an Application Load Balancer (ALB) across multiple Public Subnets in different AZs. | 06/06/2026 | 06/06/2026 | |
| 3 | Configure Target Groups targeting port `8080` with HTTP health checks pointing to `/api/health`. | 08/06/2026 | 08/06/2026 | |
| 4 | Capture an Amazon Machine Image (AMI) from the configured backend EC2 server instance. | 09/06/2026 | 09/06/2026 | [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) |
| 5 | Setup an EC2 Launch Template and define an Auto Scaling Group (ASG) with a minimum of 1 and maximum of 3 instances. | 10/06/2026 | 10/06/2026 | [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) |
| 6 | Apply Target Tracking scaling policies (scale out when average CPU utilization exceeds 70%) and verify ALB endpoint resolution. | 11/06/2026 | 11/06/2026 | |

### Achievements
- Successfully deployed an Application Load Balancer providing resilient traffic routing to active Target Groups.
- Built a standardized AMI snapshot of the backend host environment.
- Activated an Auto Scaling Group with CPU-triggered scaling rules to protect against service outages under peak loads.