require("dotenv").config({ path: ".env.service.local" });

let Service = require("node-windows").Service;

let svc = new Service({
  name: "Test Node Service",
  description: "Test Node Service",
  script: require("path").join(__dirname, "server.js"),
});

svc.on("install", () => {
  console.log("Service installed");
  console.log("Test Node Service exists: ", svc.exists);
  svc.start();
});

// svc.logOnAs.account = process.env.ADMIN_USER;
// svc.logOnAs.password = process.env.ADMIN_PASSWORD;

svc.install();
