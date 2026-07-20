---
title: "Worklog Week 5"
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Core Objectives
- Create secure object storage environments using Amazon S3.
- Configure S3 Buckets for hosting static assets and static websites.
- Build and upload the ReactJS frontend build artifacts and pet image repositories to their respective Buckets.

### Worklog Table

| Day | Task | Start Date | End Date | References |
|-----|------|------------|----------|------------|
| 1 | Learn about Amazon S3 architecture, storage classes, and bucket security (Bucket Policies, ACLs). | 15/05/2026 | 15/05/2026 | [Amazon S3 Docs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) |
| 2 | Create `pet-resort-frontend` S3 bucket to store static ReactJS build assets. | 16/05/2026 | 16/05/2026 | |
| 3 | Create `pet-resort-media` S3 bucket specifically designated for pet care images and assets. | 18/05/2026 | 18/05/2026 | |
| 4 | Enable "Static website hosting" on the frontend bucket and configure a temporary public read bucket policy for deployment testing. | 19/05/2026 | 19/05/2026 | |
| 5 | Run the ReactJS production build locally (`npm run build`) and upload the build bundle (`dist` or `build`) to the frontend bucket. | 20/05/2026 | 20/05/2026 | |
| 6 | Validate S3 static website endpoints, upload pet images to the media bucket, and test resource accessibility. | 21/05/2026 | 21/05/2026 | |

### Achievements
- Successfully provisioned two separate S3 buckets dedicated to Frontend hosting and Media storage.
- Successfully built and deployed the ReactJS web application to S3 Static Website Hosting.
- Verified that static assets and images load smoothly via direct S3 URLs.