# Centralized Secret Management System using AWS Secrets Manager and IAM Policies

---

## 📌 Project Overview

This project demonstrates how to eliminate **hardcoded secrets** from application code and implement **secure centralized secret management using AWS Secrets Manager and IAM Roles**.

The application dynamically retrieves database credentials from **AWS Secrets Manager**, ensuring that sensitive information is **never stored in source code or configuration files**.

---

## 🎯 Objective

Implement a secure secret management system where:

- Applications retrieve secrets dynamically
- No credentials are stored in the code
- Access to secrets is controlled using IAM roles
- Only authorized resources can access sensitive data

---

## 📂 Project Structure

```
centralized-secret-management
├── README.md
├── requirements.txt
├── app
│   ├── app_insecure.py
│   └── app_secure.py
├── iam
│   └── secrets_manager_policy.json 
├── screenshots
│   ├── secret_created.png
│   ├── iam_policy.txt
│   ├── ec2_iam_role.png
│   └── secret_retrieval.png

```

### 1️⃣ Application Setup

Steps performed:

- Launch an **EC2 instance**
- Install required dependencies
- Deploy a simple application that connects to a database
- Demonstrate **hardcoded credentials (insecure version)** for comparison

⚠️ This approach is insecure because credentials are exposed in the application code.

---
## ⚙️ Setup Instructions

Follow these steps to run the project on an Ubuntu EC2 instance.

### 1️⃣ Update the System

```bash
sudo apt update && sudo apt upgrade -y
```

### 2️⃣ Install Required Packages

```bash
sudo apt install -y python3 python3-pip python3-venv awscli unzip curl
```

### 3️⃣ Install AWS CLI

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

Verify installation:

```bash
aws --version
```

### 5️⃣ Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 7️⃣ Run the Application

Run insecure version (for comparison):

```bash
python3 app_insecure.py
```

Run secure version:

```bash
python3 app_secure.py
```

The secure application retrieves credentials dynamically from **AWS Secrets Manager** using an **IAM Role**, eliminating the need for hardcoded secrets.

## 🔐 Secrets Manager Setup

AWS Secrets Manager is used to securely store sensitive credentials.

**Secrets stored:**

- Database Username
- Database Password

---

## 👤 IAM Role Configuration

An **IAM Role** is created and attached to the EC2 instance.

Permissions granted:

- Access only to the required secret
- Follows the **least privilege principle**

---

## 🔄 Application Modification

The application is updated to **fetch credentials dynamically from AWS Secrets Manager**.

Instead of storing credentials in code, the application retrieves them securely using the **AWS SDK (Boto3)**.

---

## 🔍 Security Validation

Security checks performed:

- Application works **without hardcoded credentials**
- Secrets retrieved dynamically from **AWS Secrets Manager**
- No **AWS access keys stored on the server**
- Access controlled via **IAM role**
- Follows the **least privilege principle**

---

## 🛠️ Technologies & Tools

- AWS EC2
- AWS Secrets Manager
- AWS IAM
- Python
- Flask
- Boto3 SDK

---

## 📸 Screenshots

Include the following screenshots in the repository:

- Secret stored in **AWS Secrets Manager**
- IAM Policy allowing access to the secret
- EC2 IAM Role attachment
- Application retrieving secret from Secrets Manager
- Application running successfully

---

## 🔐 Security Improvements Achieved

| Before Implementation | After Implementation |
|----------------------|----------------------|
| Passwords stored in code | Secrets stored in AWS Secrets Manager |
| Hardcoded credentials | Dynamic secret retrieval |
| Shared credentials | IAM controlled access |
| Security risk | Centralized secure management |

---

## ✅ Conclusion

This project demonstrates a secure and scalable approach to managing application secrets using AWS services.

By eliminating hardcoded credentials and implementing centralized secret management with IAM-controlled access, the system significantly improves security and reduces the risk of credential exposure.

The solution follows DevSecOps best practices and ensures that sensitive data remains protected while still being accessible to authorized applications.
