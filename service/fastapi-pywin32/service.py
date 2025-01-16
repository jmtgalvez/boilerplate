import os
import sys
import site

service_directory = os.path.dirname(__file__)
source_directory = os.path.abspath(service_directory)
os.chdir(source_directory)
venv_base = os.path.abspath(os.path.join(source_directory, ".venv"))
sys.path.append(".")
old_os_path = os.environ['PATH']
os.environ['PATH'] = os.path.join(venv_base, "Scripts") + os.pathsep + old_os_path
site_packages = os.path.join(venv_base, "Lib", "site-packages")
prev_sys_path = list(sys.path)
site.addsitedir(site_packages)
sys.real_prefix = sys.prefix
sys.prefix = venv_base

new_sys_path = list()
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[: 0] = new_sys_path

import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import uvicorn
import logging
import pathlib

from app import app

class AppServerSvc(win32serviceutil.ServiceFramework):
  _svc_name_ = "APIServerSvc"
  _svc_display_name_ = "API Server"

  def __init__(self, args):
    win32serviceutil.ServiceFramework.__init__(self,args)
    self.hWaitStop = win32event.CreateEvent(None,0,0,None)
    socket.setdefaulttimeout(60)

  def SvcStop(self):
    self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
    win32event.SetEvent(self.hWaitStop)

  def SvcDoRun(self):
    servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_,''))
    self.main()

  def main(self):
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    win32serviceutil.HandleCommandLine(AppServerSvc)
  else:
    servicemanager.Initialize()
    servicemanager.PrepareToHostSingle(AppServerSvc)
    servicemanager.StartServiceCtrlDispatcher()