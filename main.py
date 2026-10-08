from orchestrator.runner import run_in_sandbox
from orchestrator.evaluator import generate_audit_report

if __name__ == "__main__":
    target_script = "tests/test_workload.py"
    
    print("[*] Launching SurakshaAgent Auditor...")
    logs = run_in_sandbox(target_script)
    
    print("\n--- Sandbox Raw Output ---")
    print(logs)
    print("--------------------------")
    
    generate_audit_report(logs)