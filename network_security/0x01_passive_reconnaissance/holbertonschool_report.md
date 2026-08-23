# Passive Reconnaissance Report: holbertonschool.com

## 1. Executive Summary
This report summarizes the passive reconnaissance findings for the domain `holbertonschool.com` gathered using **Shodan**. The objective is to identify IP ranges, associated infrastructure, and the web technologies/frameworks utilized across its subdomains.

---

## 2. IP Ranges & Infrastructure
Through Shodan search queries (such as `hostname:holbertonschool.com` and `ssl:holbertonschool.com`), the following primary IP addresses and associated ranges/providers were identified:

* **Primary IP Ranges / Subnets:**
  * `99.83.128.0/18` (AWS Global Accelerator / Amazon.com)
  * `75.2.0.0/15` (AWS Global Accelerator / Amazon.com)
  * `151.139.128.0/18` (Highwinds / StackPath CDN)
  * `192.0.64.0/18` (Automattic / WordPress Infrastructure)
  * `104.16.0.0/12` (Cloudflare, Inc.)
  * `54.80.0.0/12` / `52.0.0.0/10` (AWS EC2 - us-east-1)
  * `13.36.0.0/14` (AWS EC2 - eu-west-3)

---

## 3. Technologies & Frameworks
Analysis of HTTP headers, SSL certificates, and banners on Shodan revealed the following technologies, web servers, and frameworks used across `holbertonschool.com` subdomains:

### **Web Servers & CDNs**
* **Nginx** (Reverse proxy and web application hosting)
* **Cloudflare** (DNS, DDoS protection, and edge caching)
* **Amazon CloudFront / AWS Global Accelerator** (Content delivery and routing)
* **StackPath / Highwinds CDN** (Static asset distribution)

### **Content Management Systems (CMS) & Platforms**
* **WordPress** (Used for main landing pages and blog subdomains)
* **Webflow** (Marketing and landing pages)
* **Discourse** (Community forum software)
* **Zendesk** (Helpdesk and support infrastructure)

### **Backend Frameworks & Technologies**
* **Ruby on Rails** (Core application logic and student portal)
* **Node.js / Express** (API endpoints and microservices)
* **Phusion Passenger / Puma** (Application servers for Rails)

### **Security & Analytics Protocols**
* **TLS/SSL Certificates:** Let's Encrypt, Amazon Trust Services, Cloudflare Inc.
* **SPF / DKIM / DMARC:** Google Workspace (`aspmx.l.google.com`), Mailgun, Exclaimer.

---

## 4. Conclusion & Recommendations
The infrastructure of `holbertonschool.com` is heavily distributed across cloud providers (primarily AWS and Cloudflare) with distinct technology stacks depending on the subdomain purpose (e.g., Rails for main platform, Webflow/WordPress for marketing). 

* **Recommendation:** Ensure all legacy subdomains (e.g., staging environments) on AWS EC2 instances are regularly patched and monitored on Shodan for open ports and exposed administrative interfaces.
