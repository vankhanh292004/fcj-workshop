---
title: "Week 8 Worklog"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:
* Complete packaging the Spring Boot source code of the Pet Resort & Care project into an independent executable file (.jar) directly on the local machine.
* Research and compare Backend deployment solutions: PaaS (AWS Elastic Beanstalk) vs IaaS (Amazon EC2).
* Practice basic Linux commands (`pscp`, `chmod`, `ping`) and explore EC2 Instance Store storage.
* Configure AWS network infrastructure (VPC Route Tables, Transit Gateway) to prepare the actual deployment environment as guided by the mentor.

### Tasks Performed During the Week:

| Day | Detailed Tasks | Start Date | End Date | References |
| :--- | :--- | :--- | :--- | :--- |
| 1 | - Practice Linux command line: Use the `pscp` tool on Windows to copy the security key file (`.pem`/`.ppk`) to the `/home/ec2-user/` directory of the EC2 server.<br>- Set up SSH security using the `chmod 400` command for the key file and use `ping amazon.com` to test network connectivity. | 08/06/2026 | 08/06/2026 | Linux Command Line Guide |
| 2 | - Set up network infrastructure on the AWS VPC Console.<br>- Configure **VPC Route Tables** for independent networks (First, Second, Third, Fourth VPC) and route the traffic (`0.0.0.0/0`) centrally to the **Transit Gateway**. | 09/06/2026 | 09/06/2026 | AWS VPC & Transit Gateway |
| 3 | - Pause coding new features to start learning the Build and Packaging process for a Spring Boot application.<br>- Read documentation on Maven Lifecycle (Clean, Compile, Package). | 10/06/2026 | 10/06/2026 | Spring Boot Maven Documentation |
| 4 | - Practice running the command `mvn clean package` in the VS Code / IntelliJ Terminal to package the Pet Shop Backend project into a `.jar` file.<br>- Resolve minor errors related to Test Cases during the build process. | 11/06/2026 | 11/06/2026 | StackOverflow / Java Blogs |
| 5 | - Close the IDE, open Windows Command Prompt, and try running the newly built `.jar` file using the command `java -jar petshop-backend.jar`.<br>- Recheck the APIs on Postman to ensure the independent file runs smoothly. | 12/06/2026 | 12/06/2026 | Java Documentation |
| 6 | - Briefly explore **AWS Elastic Beanstalk** (PaaS) — an automated solution that helps upload `.jar` files via a Web interface.<br>- Compare the pros and cons between Beanstalk and **Amazon EC2** (IaaS). | 13/06/2026 | 13/06/2026 | AWS Elastic Beanstalk Guide |
| 7 | - After consulting with the mentor, decide to deploy directly on **Amazon EC2** to maximize practical learning value.<br>- Research the characteristics of **EC2 Instance Store**: high-speed NVMe drive but loses data when the instance is stopped (not suitable for the main database). | 14/06/2026 | 14/06/2026 | Amazon EC2 & Storage Docs |

### Week 8 Achievements:

* **Mastered Local Application Packaging:** Successfully used Maven to build the project into a `.jar` file and ran it independently via the command line.
* **Developed Cloud Service Selection Mindset:** Differentiated between IaaS and PaaS, and clearly understood the "ephemeral" nature of Instance Store data to strategize safe storage options for the database.
* **Mastered Network & Linux Server Configuration:** Successfully performed remote file transfer (`pscp`), set up security permissions (`chmod 400`), and established central routing between VPCs via Transit Gateway.
* **Defined Deployment Roadmap:** Following the mentor's advice, the team has prepared the basic network infrastructure and EC2 server, laying the groundwork for deploying the project to the cloud environment next week.