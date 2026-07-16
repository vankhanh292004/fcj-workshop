---
title: "Worklog Week 4"
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

Core Objectives of Week 4:
- Research Virtual Private Cloud (VPC) infrastructure to build a secure and isolated deployment environment for the system.
- Deploy Amazon RDS relational database (MySQL engine) serving the Pet Resort & Care project.
- Configure foundational Security Groups to establish a firewall layer protecting the data.

| Day | Task | Start Date | End Date | Reference Material |
|-----|------|------------|----------|--------------------|
| 1 | Study fundamental concepts of Amazon VPC, the principles of networking allocation into Public Subnets (receiving external traffic) and Private Subnets (hiding the Database). | 11/05/2026 | 11/05/2026 | Amazon VPC Documentation |
| 2 | Explore Amazon RDS database service, evaluating the benefits of using a Managed RDS Service compared to self-operating MySQL on EC2. | 12/05/2026 | 12/05/2026 | Amazon RDS Documentation |
| 3 | Initialize an Amazon RDS MySQL database instance (applying Single-AZ configuration within the Free Tier to optimize the internship budget). | 13/05/2026 | 13/05/2026 | AWS RDS Console |
| 4 | Configure the Security Group for the Database: Restrict access permissions only from internal IP ranges or authorized servers, completely blocking direct connections from the Internet. | 14/05/2026 | 14/05/2026 | AWS Security Best Practices |
| 5 | Verify connection information (Endpoint URL) of the Database; prepare core data table structures (User, Pet, Order) to be ready for backend integration. | 15/05/2026 | 15/05/2026 | |

Achievements of Week 4:

• Finalized network planning and secure architecture design mindset on the Cloud environment based on the VPC model and strict subnet segregation strategies.

• Successfully launched the MySQL database management system on the Amazon RDS platform (Single-AZ mode), ensuring technical requirements are met while maximizing credit savings.

• Successfully applied a firewall layer using Security Groups, creating a robust shield to protect the Database instance from unauthorized access threats outside the network.