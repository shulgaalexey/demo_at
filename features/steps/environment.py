from behave import given, then
import subprocess
import telnetlib

process = None

def is_port_open(host, port):
    try:
        tn = telnetlib.Telnet(host, port)
        tn.close()
        return True
    except:
        return False
    
    
@given('Knowledge Service is up and running')
def ensure_knowledge_svc_is_up(context):
    if is_port_open("localhost", 18082):
        print("Starting Knowledge Service")
        process = subprocess.Popen(["python", "../../knowledge_svc_mock.py"])
        print("process id: " + str(process.pid))
        assert process.pid > 0
    else:
        print("Knowledge Service is already running")
        #ensure_knowledge_svc_is_down(context)
        #process = None


@then('Knowledge Service should be stopped')
def ensure_knowledge_svc_is_down(context):
    print("Stopping Knowledge Service")
    if process: process.terminate()