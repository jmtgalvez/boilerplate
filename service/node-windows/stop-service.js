let Service = require("node-windows").Service;

let svc = new Service({
  name: "Test Node Service",
  script: require("path").join(__dirname, "server.js"),
});

svc.on("uninstall", () => {
  console.log("Service uninstall complete");
  console.log("Test Node Service exists: ", svc.exists);
});

svc.uninstall();
