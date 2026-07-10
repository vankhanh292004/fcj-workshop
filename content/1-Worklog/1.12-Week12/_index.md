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
##### Week 5 (18/05 – 24/05): AWS Compute Services — EC2 vs Lambda
* Studied **Subnets** in VPC in depth: Classified Public, Private, VPN-only Subnets and IP allocation rules (CIDR, AWS's 5 reserved IPs).
* Explored **NAT Gateway** combined with **Elastic IP** to provide secure Internet access for resources in Private Subnets.
* Read comprehensive documentation on **Amazon EC2**: Instance Lifecycle, operational states, and **Key Pair** security mechanisms.
* Studied **Serverless** concepts and the event-driven execution model of **AWS Lambda**.
* Performed theoretical comparative analysis between **EC2** and **Lambda** regarding infrastructure management, auto-scaling mechanisms, and cost calculations.
* Team discussion concluded: The Spring Boot application (Pet Resort project) is better suited for **EC2** (running in Private Subnet via NAT Gateway) rather than Serverless Lambda.

##### Week 6 (25/05 – 29/05): Core Knowledge Review, CloudFront & Architecture Drafting
* Attended office for self-study sessions; systematized account security configurations; verified MFA setup and IAM access policies.
* Reviewed **Amazon S3** in depth: Object Lifecycle Policies and Bucket security mechanisms.
* Team discussions on VPC models; revisited Subnet segmentation theory and **Security Groups** firewall rules.
* Explored static Frontend distribution solutions: Compared standard **S3 Static Hosting** versus **AWS Amplify** integration.
* Determined direction: Use **Amazon S3 + CDN (CloudFront)** for the ReactJS Frontend to optimize costs.

##### Week 7 (01/06 – 05/06): Frontend-Backend Integration, JWT & E2E Testing
* Connected **React Frontend** display pages with **Spring Boot** APIs through the intermediary layer `services/api.js`; configured **Axios base URL** pointing to the Backend.
* Built complete **Login/Register** flows (`LoginPage`, `RegisterPage`); integrated **JWT** authentication token handling (`JwtResponse`, `JwtTokenProvider`) from `AuthController` into the Frontend's `authStore.js`.
* Connected product catalog pages (`ProductsPage`, `ProductCard`) with dynamic data from `ProductController`; implemented cart logic for `CartPage` via `cartStore.js`.
* Built order processing (`CheckoutPage`) and pet care booking (`BookingPage`) flows; connected to `OrderController` and `BookingController`.
* Completed comprehensive **End-to-End Testing** of the customer journey: **Register → Login → Add to Cart → Book Spa → Process Payment**.
* Optimized `CorsConfig` to thoroughly resolve **CORS** errors between Frontend and Backend environments.

##### Week 8 (08/06 – 12/06): Spring Boot Packaging (.jar) & Beanstalk vs EC2 Evaluation
* Paused new feature development; began studying the **Build and Package** process for Spring Boot applications; read **Maven Lifecycle** documentation (Clean, Compile, Package).
* Practiced running `mvn clean package` to package the Backend project into a `.jar` file; resolved Test Case errors during the build process.
* Closed the IDE, opened **Command Prompt** and ran the `.jar` file with `java -jar petshop-backend.jar`; verified all APIs on Postman to ensure standalone execution.
* Explored **AWS Elastic Beanstalk** (PaaS): An automated solution for uploading `.jar` files via the Web interface without Linux command-line expertise.
* Compared benefits/limitations between **Beanstalk** (easy but less control) and **EC2** (harder but more educational).
* Following **Mentor** consultation, the team decided to deploy directly on **Amazon EC2** instead of Beanstalk — hands-on Linux server configuration, Security Groups, and Load Balancer setup provides greater learning value.

---

#### PHASE 3: CLOUD DEPLOYMENT & AUTOMATION (Weeks 9 – 12)

##### Week 9 (15/06 – 21/06): S3 Bucket Initialization, Code Security & Error Handling
* Studied **Amazon S3** (Simple Storage Service) fundamentals: Bucket, Object, Key concepts and common use cases.
* Practiced creating an S3 Bucket on AWS Console: Entered the name `aws-first-cloud-journey`, configured region **ap-southeast-1 (Singapore)**, set **Object Ownership** to **ACLs disabled** per AWS recommendations.
* Documented a key lesson: S3 Bucket names must be **globally unique**. When a duplicate name is entered, the system displays a red error *"Bucket with the same name already exists"* — requiring numeric suffixes to avoid collisions.
* Reviewed and optimized `ProductServiceImpl` and `BookingServiceImpl` service layers; resolved **N+1 Query** issues in JPA/Hibernate.
* Secured `application.yml`: Extracted sensitive information (DB URL, Username, Password, JWT Secret Key) from source code into **system Environment Variables**.
* Refined the centralized `GlobalExceptionHandler` error filter and ran Postman tests with edge-case scenarios.

##### Week 10 (22/06 – 28/06): CloudFront Configuration, Architecture Refinement & Community Review
* Studied **Amazon CloudFront**: CDN (Content Delivery Network), Edge Location, Distribution concepts and static content acceleration.
* Practiced creating a **CloudFront Distribution**: Pointed the Origin to the S3 Bucket `aws-first-cloud-journe...` from the previous week. Distribution successfully created with ID **E2NI0FJ3HELT9Z**, Status **Enabled** and **Deploying**.
* Analyzed the actual source code structure to draft functional tier layers; sketched the initial architecture blueprint on **Draw.io** with CloudFront + S3 flow integration.
* Browsed the **AWS Study Group** community to evaluate prior cohort architecture blueprints; compiled common design pitfalls from Admin review comments.
* Visualized application flow: **Route 53 → S3/CloudFront → RESTful API → Backend → RDS MySQL**.
* Eliminated redundant architectural components (Lambda, DynamoDB from templates) that didn't match the team's Spring Boot codebase.

##### Week 11 (29/06 – 04/07): CloudFormation (IaC), Architecture Finalization & Cloud Deployment
* Received feedback from Admin: Fixed CloudFront flow for Frontend and Media distribution; finalized the AWS architecture blueprint.
* Studied **AWS CloudFormation**: Stack, Template (YAML/JSON) concepts and the **Infrastructure as Code** automated resource provisioning workflow.
* Practiced creating a Stack on CloudFormation Console: Configured parameters **AvailabilityZone** (`us-east-1a`), **LatestAmiId** (Amazon Linux 2 AMI), **NotificationEmail**, **S3BucketName**, **S3KeyLambdaZip**.
* Uploaded to S3 Bucket `aws-backup-lab13-fcj` two files: `backup-lab.yaml` (infrastructure template) and `lambda_function.zip` (processing code) in the `Backup Plan/` directory.
* Stack `backup-plan-lab13` initialized on October 27, 2024; components **LambdaRole**, **SNSTopic**, **Instance**, **Route** all reached **CREATE_COMPLETE** status.
* **Deployed the entire system to AWS production:**
  * Network & Security Layer: VPC, Public/Private Subnets (Multi-AZ), NAT Gateway, Security Groups, IAM Roles, KMS, Secrets Manager.
  * Data Tier: Amazon RDS MySQL (Multi-AZ, Sync Replication), ElastiCache Redis (Cache-Aside).
  * Compute Tier: EC2 + Auto Scaling Group + Application Load Balancer (ALB).
  * Edge Layer: S3 Frontend + S3 Media + CloudFront + AWS WAF.
* Successfully applied **Zero Trust** security principles: No SSH (Port 22) open, Database hidden in Private Subnet, credentials managed via Secrets Manager.

##### Week 12 (06/07 – 10/07): Load Testing, Monitoring, FinOps & Project Wrap-up
* Comprehensive E2E testing, load testing, CloudWatch Dashboards + SNS Alarms configuration.
* Resource optimization (FinOps), cleanup of unused resources; finalized technical documentation and prepared for project defense.

---

#### Quick 12-Week Summary Table:

| Week | Period | Main Focus | AWS Skills & Services |
|------|--------|------------|----------------------|
| 1 | 17/04 – 23/04 | AWS onboarding & environment setup | AWS Free Tier, IAM, Hugo, EC2 basics |
| 2 | 24/04 – 30/04 | Account security & cost management | MFA, Root User, Admin Group, AWS CLI, Budgets |
| 3 | 01/05 – 07/05 | Amazon S3 & detailed AWS Budgets | S3 (`petshop-media-storage`), 4 Budget types |
| 4 | 11/05 – 15/05 | VPC, RDS MySQL & Security Groups | VPC, Public/Private Subnet, RDS MySQL, SG |
| 5 | 18/05 – 24/05 | Compute Services: EC2 vs Lambda | Subnet, NAT Gateway, EC2 Lifecycle, Lambda |
| 6 | 25/05 – 29/05 | Review & architecture drafting | IAM/S3/VPC/EC2 review, S3 Static Hosting, CDN |
| 7 | 01/06 – 05/06 | Frontend-Backend integration & JWT | ReactJS + Spring Boot, JWT Auth, E2E Testing |
| 8 | 08/06 – 12/06 | .jar packaging & service selection | Maven, `.jar`, Beanstalk vs EC2, chose EC2 |
| 9 | 15/06 – 21/06 | S3 Bucket & code security | S3 `aws-first-cloud-journey`, ACLs, env vars |
| 10 | 22/06 – 28/06 | CloudFront & architecture refinement | CloudFront Distribution, Draw.io, community review |
| 11 | 29/06 – 04/07 | CloudFormation (IaC) & cloud deploy | CloudFormation Stack, VPC Multi-AZ, full deploy |
| 12 | 06/07 – 10/07 | Load Test, Monitoring & wrap-up | CloudWatch, SNS, FinOps, project defense |

---

#### AWS Services Used Throughout the Project:

| Service Category | Specific Services | Role in the Project |
|-----------------|-------------------|---------------------|
| **Compute** | Amazon EC2, Auto Scaling Group | Running Spring Boot Backend, auto-scaling based on traffic load |
| **Storage** | Amazon S3 | Hosting static Frontend (ReactJS), pet images, invoices, CloudFormation templates |
| **Database** | Amazon RDS MySQL, ElastiCache (Redis) | Relational data storage (Multi-AZ), high-performance caching |
| **Networking & CDN** | Amazon VPC, CloudFront, Route 53, ALB, NAT Gateway | Secure network segmentation, global content delivery, load balancing |
| **Security** | IAM, Security Groups, KMS, Secrets Manager, AWS WAF, MFA | Access control, firewalls, data encryption, web application protection |
| **Monitoring** | Amazon CloudWatch, SNS | Monitoring dashboards for CPU/Memory/Network, incident email alerts |
| **Automation (IaC)** | AWS CloudFormation | Automated infrastructure deployment via YAML templates (`backup-lab.yaml`) |
| **Cost Management** | AWS Budgets, Billing Console | Budget control (Cost/Usage/RI/Savings Plans), spending threshold alerts |