# Centralized Secret Management System using AWS Secrets Manager and IAM Policies

## 📌 Project Overview

This project demonstrates how to eliminate **hardcoded secrets** from application code and implement **secure centralized secret management** using **AWS Secrets Manager** and **IAM Roles**.

The application dynamically retrieves database credentials from AWS Secrets Manager, ensuring that **sensitive information is never stored in source code or configuration files**.

---

## 🧩 Scenario

You joined as a **DevSecOps Engineer**. During an internal security audit, it was discovered that developers were storing **database passwords directly inside application configuration files**.

The **CISO** instructed the team:

> "Eliminate hardcoded secrets and implement centralized secure secret management with controlled access."

---

## 🎯 Objective

Implement a secure secret management system where:

* Applications **retrieve secrets dynamically**
* **No credentials are stored in code**
* Access to secrets is controlled using **IAM roles**
* Only authorized resources can access sensitive data

---

## ⚙️ Project Implementation

1️⃣ Application Setup
Steps performed:

* Launch an **EC2 instance**
* Install required dependencies
* Deploy a simple application that connects to a database
* Demonstrate **hardcoded credentials (insecure version)** for comparison 

⚠️ This approach is insecure because credentials are exposed in code.

---

## 🔐 Secrets Manager Setup

Secrets Manager is used to securely store sensitive credentials.
Secret Stored:
* Database Username
* Database Password.

---

## 👤  IAM Role Configuration

An **IAM Role** is created and attached to the EC2 instance.

Permissions granted:

* Access to **only the required secret**
* Follow **least privilege principle**

---

## 🔄  Application Modification

The application is updated to **fetch credentials dynamically** from AWS Secrets Manager.
This application retrieves credentials dynamically instead of storing them in the code.

---

## 🔍  Security Validation

Security checks performed:
* Application works without hardcoded credentials
* Secrets retrieved dynamically from AWS Secrets Manager
* No AWS access keys stored on the server
* Access controlled via IAM role
* Follows least privilege principle

---

## 🛠️ Technologies & Tools

* AWS EC2
* AWS Secrets Manager
* AWS IAM
* Python
* Flask
* Boto3 SDK

---

## 📸 Screenshots

Include the following screenshots in the repository:

* Secret stored in **AWS Secrets Manager**
* IAM Policy allowing access to secret
* EC2 IAM Role attachment
* Application retrieving secret from Secrets Manager
* Application running successfully

---

## 🔐 Security Improvements Achieved

| Before Implementation    | After Implementation                  |
| ------------------------ | ------------------------------------- |
| Passwords stored in code | Secrets stored in AWS Secrets Manager |
| Hardcoded credentials    | Dynamic secret retrieval              |
| Shared credentials       | IAM controlled access                 |
| Security risk            | Centralized secure management         |

---

## ✅ Conclusion

This project demonstrates a **secure and scalable approach to managing application secrets** using AWS services. By eliminating hardcoded credentials and implementing **centralized secret management with IAM-controlled access**, the system significantly improves security and reduces the risk of credential exposure.

The solution follows **DevSecOps best practices** and ensures that sensitive data remains protected while still being easily accessible to authorized applications.
