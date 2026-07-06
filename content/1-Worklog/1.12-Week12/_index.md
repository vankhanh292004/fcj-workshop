---
title: "Worklog Week 12"
weight: 12
chapter: false
pre: " <b> 1.12. </b> "
---

### Week 12 Objectives:
* Complete the monitoring configuration and conduct Load Testing for the *Pet Resort & Care System* on the AWS environment.
* Perform cost optimization (FinOps) by cleaning up unused resources and temporary testing assets.
* Summarize the knowledge gained over the 12-week internship, finalize technical documentation, and prepare slides/scripts for the final project defense and acceptance report.

### Tasks to be implemented this week:
| Day | Task | Start Date | End Date | References |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ----------------------------------------- |
| Monday | - End-to-End Testing: Run smoke tests to verify purchasing flows, spa booking, payments, and connection stability from Frontend (CloudFront) to Backend (ALB). | 06/07/2026   | 06/07/2026      | Team's Test Case Scripts                  |
| Tuesday | - Setup Monitoring & Alerting: Configure Amazon CloudWatch Dashboards and create SNS Alarms to send email alerts to Admins when EC2 CPU or RDS connections exceed 80%.                      | 07/07/2026   | 07/07/2026      | AWS Documentation (CloudWatch, SNS)       |
| Wednesday | - Load Testing: Simulate sudden high traffic (e.g., Flash Sale) to verify the EC2 Auto Scaling mechanism and the caching efficiency of ElastiCache (Redis).                                 | 08/07/2026   | 08/07/2026      | Apache JMeter / Postman                   |
| Thursday | - Resource Optimization (FinOps): Clean up temporary resources (test buckets, old snapshots, unattached Elastic IPs) to keep running costs under the budget limit (~$168/month).              | 09/07/2026   | 09/07/2026      | AWS Billing Console                       |
| Friday | - Finalize Deliverables: Write the deployment README, finalize the Architecture Blueprint document, and prepare the Slide + Demo script for the final project defense.                        | 10/07/2026   | 10/07/2026      | Project Documentation                     |

### Achievements in Week 12:

* **Basic Project Completion:** The *Pet Resort & Care System* is now operational and fulfills the core feature requirements. During Load Testing, the Auto Scaling mechanism functioned; however, we realized the scale-out speed sometimes experiences slight delays, highlighting a need for further configuration optimization in the future.
* **Monitoring & Cost Optimization:** Successfully set up incident alerts via CloudWatch & SNS and cleaned up unused resources. Nevertheless, our logging system is still somewhat fragmented and lacks a centralized log analysis tool (like the ELK stack).
* **Acknowledging Shortcomings & Lessons Learned:** Looking back over the 12 weeks, I humbly recognize significant room for improvement in code optimization, fully automated CI/CD pipelines, and mitigating potential security risks. The current knowledge serves only as a foundational starting point.
* **Internship Wrap-up:** Finalized all technical deliverables and prepared a receptive mindset for the final defense. This milestone is an essential stepping stone for diving deeper into advanced technologies like Containerization (Docker/EKS) and Microservices post-internship.