---
title: "Worklog Week 8"
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:
* Complete the packaging process of the Pet Resort & Care Spring Boot source code into an executable archive (.jar) on the local environment.
* Research cloud deployment solutions for hosting the backend application: compare PaaS (AWS Elastic Beanstalk) vs IaaS (Amazon EC2).
* After receiving mentor guidance, pivot towards deploying directly on Amazon EC2 to gain deeper hands-on infrastructure experience.

### Tasks carried out this week:
| Day | Detailed Task | Start Date | Completion Date | Reference Material |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | --------------- | ----------------------------------------- |
| 1 | - Pause feature development to study the Build and Packaging lifecycle of a Spring Boot application.<br>- Read documentation covering Maven Lifecycles (Clean, Compile, Package). | 08/06/2026 | 08/06/2026 | Spring Boot Maven Docs |
| 2 | - Practice executing the `mvn clean package` command within the VS Code / IntelliJ terminal to build the Pet Shop backend into a `.jar` file.<br>- Resolve minor build failures related to skipped Test Cases. | 09/06/2026 | 09/06/2026 | StackOverflow / Java Blogs |
| 3 | - Close the IDE completely, open Windows Command Prompt, and execute the generated binary using the `java -jar petshop-backend.jar` command.<br>- Retest API endpoints via Postman to ensure stable standalone execution. | 10/06/2026 | 10/06/2026 | Java Documentation |
| 4 | - Initially explored **AWS Elastic Beanstalk** (PaaS) as a simpler deployment option that handles EC2 provisioning automatically.<br>- Compared with raw Amazon EC2 deployment: Beanstalk is easier but offers less control and learning value. | 11/06/2026 | 11/06/2026 | AWS Elastic Beanstalk Guide |
| 5 | - After consulting with mentors, the team decided to deploy directly onto **Amazon EC2** instead of Beanstalk. The reasoning: manually configuring Linux servers, Security Groups, and Load Balancers provides far more valuable hands-on experience for the internship goals. | 12/06/2026 | 12/06/2026 | Amazon EC2 Linux Docs |

### Week 8 Achievements:

* **Mastered Local Application Packaging Skills:**
  * Understood the operational difference between running source code inside an IDE versus executing an independently compiled binary.
  * Successfully utilized Apache Maven to compile and package the Spring Boot project into a complete, standalone `.jar` executable.
  * Ensured the backend application runs stably on the local Windows environment using the `java -jar` protocol, successfully connecting to the local database.

* **Developed Cloud Service Evaluation Mindset:**
  * Grasped the fundamental differences between IaaS (Amazon EC2) and PaaS (AWS Elastic Beanstalk) deployment models.
  * Evaluated trade-offs: Beanstalk is easier but hides infrastructure details; EC2 requires more effort but maximizes learning outcomes.

* **Defined a Deployment Roadmap for Upcoming Weeks:**
  * Following mentor advice, aligned on deploying directly onto **Amazon EC2** for the Pet Resort & Care backend. Although this path demands Linux command-line skills and manual infrastructure configuration, the team recognized it as a much richer learning opportunity aligned with the internship's educational objectives.