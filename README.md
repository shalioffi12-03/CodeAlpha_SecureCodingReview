# CodeAlpha Task 3 – Secure Coding Review

## 📌 Project Overview

This project was completed as part of the **CodeAlpha Cyber Security Internship – Task 3: Secure Coding Review**.

The project demonstrates a security review of a **Python Flask login application**. The original application was inspected to identify security vulnerabilities using **manual code review and Bandit static analysis**.

After identifying the vulnerabilities, secure coding practices were applied to create an improved version of the application.

## 🎯 Objective

The main objectives of this project are:

* Review application source code for security vulnerabilities.
* Identify insecure coding practices.
* Use Bandit for static security analysis.
* Document the identified security issues.
* Apply appropriate security fixes.
* Compare the original application with the secure version.

## 🛠️ Technologies and Tools Used

* **Python**
* **Flask**
* **SQLite**
* **Bandit**
* **Manual Code Review**

## 📂 Project Files

### `app.py`

This is the **original Flask login application** that contains the security vulnerabilities identified during the review.

### `secure_app.py`

This is the **secure version of the application** in which the identified security issues have been addressed using secure coding practices.

### `security_report.md`

This file contains the complete security review report, including:

* Project overview
* Tools used
* Security findings
* Severity levels
* Risks
* Recommendations
* Security improvements
* Bandit scan results
* Conclusion

### Bandit Output Screenshots

The repository also contains screenshots showing the Bandit security scan results:

* `bandit_vulnerable.PNG`
* `bandit output 1.PNG`
* `banditop2.PNG`
* `banditop3.PNG`

These screenshots provide evidence of the security analysis performed on the application.

## 🔍 Security Vulnerabilities Identified

The original application contained three main security issues.

### 1. Hardcoded Secret

**Severity:** Low

The original application contained a secret directly in the source code.

**Risk:**
Anyone who gains access to the source code may be able to view the secret.

**Remediation:**
The secure version uses an environment variable instead of directly hardcoding the secret.

### 2. SQL Injection

**Severity:** Medium

The original application constructed the SQL query using string concatenation with user input.

**Risk:**
An attacker could potentially manipulate the SQL query through malicious input.

**Remediation:**
The secure version uses a parameterized SQL query.

### 3. Flask Debug Mode Enabled

**Severity:** High

The original application was configured with Flask debug mode enabled.

**Risk:**
Debug mode can expose sensitive application information and should not be enabled in production.

**Remediation:**
Debug mode was disabled in the secure version.

## 🔐 Security Improvements

The following security improvements were implemented:

1. Hardcoded secrets were replaced with environment-based configuration.
2. SQL string concatenation was replaced with parameterized queries.
3. Password verification was improved using password hashing.
4. Flask debug mode was disabled.

## 📊 Bandit Security Scan Results

### Original Application

The Bandit scan identified:

| Severity | Issues |
| -------- | -----: |
| High     |      1 |
| Medium   |      1 |
| Low      |      1 |

### Secure Application

After applying the security improvements, the secure application was scanned again using Bandit.

| Severity | Issues |
| -------- | -----: |
| High     |      0 |
| Medium   |      0 |
| Low      |      0 |

The final Bandit scan reported **no security issues**.

## 🔄 Original vs Secure Application

| Security Aspect       | Original Application | Secure Application              |
| --------------------- | -------------------- | ------------------------------- |
| Secret Management     | Hardcoded secret     | Environment-based configuration |
| SQL Query             | String concatenation | Parameterized query             |
| Password Verification | Direct comparison    | Password hash verification      |
| Flask Debug Mode      | Enabled              | Disabled                        |
| Bandit Result         | 3 issues             | No issues                       |

## ▶️ Project Execution

The project uses Python and Flask.

The original application can be reviewed to understand the identified insecure coding practices, while `secure_app.py` demonstrates the corresponding security improvements.

The security analysis can be performed using Bandit.

Example:

```bash
bandit app.py
```

For the secure version:

```bash
bandit secure_app.py
```

## 📚 Learning Outcomes

Through this project, I learned:

* How to perform a basic secure code review.
* How to identify common security vulnerabilities.
* How SQL injection can occur through unsafe query construction.
* Why secrets should not be hardcoded.
* Why Flask debug mode should be disabled in production.
* How password hashing improves password security.
* How Bandit can be used for Python security analysis.
* How secure coding practices can reduce application vulnerabilities.

## 📋 Internship Details

**Organization:** CodeAlpha
**Domain:** Cyber Security
**Task:** Task 3 – Secure Coding Review
**Programming Language:** Python
**Framework:** Flask
**Database:** SQLite
**Security Tool:** Bandit

## ✅ Conclusion

This project demonstrates the process of reviewing a Flask login application for security vulnerabilities and applying secure coding practices to address the identified issues.

The original application contained three security issues with High, Medium, and Low severity levels. After implementing the recommended security improvements, the secure application was scanned again using Bandit and the final scan reported **no security issues**.

This project provided practical experience in secure coding, vulnerability identification, remediation, and static security analysis.
