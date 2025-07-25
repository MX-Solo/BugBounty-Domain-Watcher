<h1 align="center">🔎 BugBounty Domain Watcher</h1>
<p align="center">
  A monitoring tool for Bug Bounty hunters to detect new subdomains and track changes in status and technologies.
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

---

## 🧠 Overview

**BugBounty Domain Watcher** is an automated system designed to help bug bounty hunters continuously monitor target domains.

It consists of two main components:

- 🖥️ `watch/`: A server that monitors subdomains and stores data in MongoDB.
- 💻 `watcher/`: A client to add/remove root domains and query monitoring results.

The goal is to **detect newly resolved subdomains**, track **status/technology changes**, and provide actionable intelligence in real time.

---

## 🧱 Architecture

```

```
       ┌────────────┐
       │  Watcher   │  ← Client CLI (Add domains / Query data)
       └────┬───────┘
            │
    ┌───────▼────────┐
    │    MongoDB     │  ← Central Database
    └───────▲────────┘
            │
     ┌──────┴──────┐
     │   Watch     │  ← Server (Monitors subdomains continuously)
     └─────────────┘
```

````

---

## 🚀 Features

### ✅ Watch (Server)
- Detects **new subdomains** (fresh discoveries)
- Tracks **HTTP status code changes**
- Tracks **technology stack changes**
- Stores all data with **timestamps** in MongoDB

### 💡 Watcher (Client)
- Add/remove domains to be monitored
- Filter results by:
  - Status codes
  - Technologies
  - Newly discovered (fresh)
  - Status or technology changes
- Query full results in JSON format

---

## ⚙️ Installation

> Requirements: Python 3.x, MongoDB (local or remote)

1. Install MongoDB  
   https://www.mongodb.com/docs/manual/installation/

2. Clone the repository:
```bash
git clone https://github.com/yourusername/bugbounty-watcher.git
cd bugbounty-watcher
````

3. Install dependencies for both components:

**For server (`watch/`)**

```bash
cd watch
pip install -r requirements.txt
```

**For client (`watcher/`)**

```bash
cd ../watcher
pip install -r requirements.txt
```

---

## 🛠️ Usage

### 1. Run the Server (Monitoring engine)

```bash
cd watch
python3 main.py
```

> The server will continuously monitor subdomains from the database and update any status or technology changes.

---

### 2. Use the Client (Watcher CLI)

#### Add a domain to be monitored

```bash
cd ../watcher
python3 main.py --domain example.com --add
```

#### Remove a domain

```bash
python3 main.py --domain example.com --remove
```

#### Query full results

```bash
python3 main.py --domain example.com --full-result
```

#### Apply filters

```bash
python3 main.py --status 403 --tech Apache --status-changed
```

#### Example Output:

```json
{
  "sub": "admin.example.com",
  "status": 403,
  "tech": "Apache",
  "fresh": true,
  "status_changed": "200 → 403",
  "tech_changed": "Nginx → Apache",
  "timestamp": {
    "$date": "2025-07-25T14:21:00.000Z"
  }
}
```

---

## 📄 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more details.

---

## 🙋 Contributing

Pull requests are welcome!
Feel free to open issues or contribute improvements and new features.

---

## ✨ Author

Made with ❤️ by \[YourName]

---

```
