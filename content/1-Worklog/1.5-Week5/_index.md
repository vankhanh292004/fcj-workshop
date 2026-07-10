---
title: "Week 5 Worklog"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:
- Finalize knowledge on cloud networking infrastructure with concepts of Subnets and NAT Gateway to establish a secure environment.
- Approach and gain an overview of Compute Services on the AWS platform.
- Research basic theories of virtual servers (Amazon EC2), serverless architecture (AWS Lambda), and how to deploy them within a virtual network space.
- Conduct a preliminary evaluation of each service's characteristics to orient the deployment solution for the backend processing later.

| Day | Task | Start Date | Completion Date | Reference Material |
|------|----------|--------------|---------------|-------------------|
| 1 | In-depth research on Subnets in VPC: Classify Public, Private, VPN-only subnets, and IP range allocation rules (CIDR, AWS's 5 reserved IPs). | 18/05/2026 | 18/05/2026 | AWS VPC Documentation |
| 2 | Understand the concept and configuration of NAT Gateway combined with Elastic IP (static IP) to provide secure Internet access for resources (like virtual servers) located in a Private subnet. | 19/05/2026 | 19/05/2026 | AWS NAT Gateway Docs |
| 3 | Read the overview documentation of Amazon EC2: Learn about the EC2 Lifecycle, operating states, and Key Pair security mechanism. | 20/05/2026 | 20/05/2026 | Amazon EC2 Docs |
| 4 | Learn the basic concepts of Serverless architecture and the event-driven operation of the AWS Lambda service. | 21/05/2026 | 21/05/2026 | AWS Lambda Docs |
| 5 | Perform a theoretical comparative analysis between EC2 and Lambda in terms of infrastructure management, auto-scaling mechanisms, and cost calculation. | 22/05/2026 | 22/05/2026 | AWS Compute Blog |
| 6 | Hold a general discussion with the team on web architecture models: Evaluate whether a Spring Boot application (like the Pet Resort project) is more suitable for EC2 (running in a Private Subnet via NAT Gateway) or Serverless Lambda. | 23/05/2026 | 23/05/2026 | |
| 7 | Systematize all theoretical knowledge learned during the week and update the progress report on the local Hugo system. | 24/05/2026 | 24/05/2026 | |

### Week 5 Achievements:

• Mastered the internal VPC network architecture, clearly understood how to divide network segments (Subnets), and grasped the essential role of the NAT Gateway in allowing virtual servers to access the Internet without being exposed externally.

• Clearly understood foundational concepts of cloud computing infrastructure, distinguishing the difference between the traditional virtual server provisioning model (EC2) and running Serverless functions (Lambda).

• Identified suitable Use Cases for each service to apply in designing a secure and cost-optimized Backend architecture for a real-world project.

• Accumulated additional overall system analysis thinking, well-prepared for the phase of finalizing the official architectural Proposal.