# Node.js as a Windows Service

This is a simple example of how to run a Node.js application as a Windows service.

## Prerequisites

- Node.js
- Windows 10 or later

## Installation

1. Install Node.js

```bash
npm install -g node-windows
```

2. Link node-windows to project

```bash
npm link node-windows
```

3. Run service.js

```bash
npm run service
```

## Stopping the service

To stop the service, run the following command:

```bash
npm run stop
```
