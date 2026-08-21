# Secure Coding Review

## 1. Project Overview

This project demonstrates a security review of a Python Flask login application.

The original application was reviewed to identify common security vulnerabilities using manual code inspection and Bandit static analysis.

---

## 2. Tools Used

- Python
- Flask
- Bandit
- SQLite
- Manual Code Review

---

## 3. Security Findings

### Finding 1: Hardcoded Secret

**Severity:** Low

**Issue:**

The application contained a secret directly inside the source code.

    SECRET_KEY = "mysecret123"

**Risk:**

Anyone who gains access to the source code may be able to view the secret.

**Recommendation:**

Store secrets using environment variables instead of hardcoding them in the source code.

---

### Finding 2: SQL Injection

**Severity:** Medium

**Issue:**

The application constructed an SQL query using string concatenation.

    query = "SELECT * FROM users WHERE username = '" + username + "'"

**Risk:**

An attacker may manipulate the SQL query through malicious user input.

**Recommendation:**

Use parameterized SQL queries.

    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

---

### Finding 3: Flask Debug Mode Enabled

**Severity:** High

**Issue:**

The application was running with Flask debug mode enabled.

    app.run(debug=True)

**Risk:**

Debug mode can expose sensitive application information and should not be enabled in production.

**Recommendation:**

Disable debug mode in production.

    app.run(debug=False)

---

## 4. Security Improvements

The following security improvements were implemented in the secure version:

1. Hardcoded secrets were replaced with environment-based configuration.
2. SQL string concatenation was replaced with parameterized queries.
3. Password verification uses password hashing.
4. Flask debug mode was disabled.

---

## 5. Security Scan Results

### Original Application

Bandit identified three security issues.

| Severity | Number of Issues |
|----------|------------------|
| High     | 1                |
| Medium   | 1                |
| Low      | 1                |

### Secure Application

The secure application was scanned again using Bandit.

**Result: No issues identified.**

| Severity | Number of Issues |
|----------|------------------|
| High     | 0                |
| Medium   | 0                |
| Low      | 0                |

---

## 6. Conclusion

The security review identified common vulnerabilities in the original Flask application.

After applying secure coding practices, the identified vulnerabilities were addressed.

The secure application was scanned using Bandit and the final scan reported no security issues.