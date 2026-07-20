---
title: "Worklog Week 6"
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Core Objectives
- Distribute static content globally with low latency using Amazon CloudFront CDN.
- Secure S3 Bucket access, restricting public S3 entries by forcing all traffic through CloudFront via Origin Access Control (OAC).
- Configure AWS WAF (Web Application Firewall) to protect the frontend application from malicious web exploits (SQLi, XSS, etc.).

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Research CloudFront operations, Edge Locations, TTL, cache behaviors, and Origin configurations. | 22/05/2026 | 22/05/2026 | [Amazon CloudFront Docs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) |
| 2 | Create a CloudFront Distribution pointing to the ReactJS static hosting S3 bucket as its origin. | 23/05/2026 | 23/05/2026 | |
| 3 | Implement Origin Access Control (OAC) and update the S3 bucket policy to only allow traffic originating from CloudFront. | 25/05/2026 | 25/05/2026 | |
| 4 | Configure custom error pages on CloudFront to route 403/404 errors back to `index.html` with a 200 status code for SPA routing. | 26/05/2026 | 26/05/2026 | |
| 5 | Study AWS WAF concepts and create a basic Web ACL configuration. | 27/05/2026 | 27/05/2026 | [AWS WAF Docs](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) |
| 6 | Attach the AWS Managed Ruleset Web ACL to the CloudFront distribution and verify rule enforcement. | 28/05/2026 | 28/05/2026 | |

### Achievements
- Enhanced page load speeds globally by caching frontend assets at CloudFront edge locations.
- Restricted direct public access to the S3 bucket, ensuring users only access the site through the CloudFront CDN endpoint.
- Deployed AWS WAF to secure the application frontend against common web threats.