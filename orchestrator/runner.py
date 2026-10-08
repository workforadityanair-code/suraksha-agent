import docker
import os

client = docker.from_env()

def run_in_sandbox(script_path: str):
    network_name = "dpi_audit_net"
    
    existing_networks = [n.name for n in client.networks.list()]
    if network_name not in existing_networks:
        client.networks.create(network_name, driver="bridge")

    abs_script = os.path.abspath(script_path)
    workdir = os.path.dirname(abs_script)
    script_file = os.path.basename(abs_script)

    print(f"[*] Spawning sandbox container for: {script_file}")

    try:
        container_output = client.containers.run(
            image="dpi-sandbox:latest",
            command=[f"/home/sandboxuser/app/{script_file}"],
            volumes={workdir: {"bind": "/home/sandboxuser/app", "mode": "ro"}},
            network=network_name,
            mem_limit="256m",
            cpu_quota=50000,
            cap_drop=["ALL"],
            security_opt=["no-new-privileges:true"],
            detach=False,
            stdout=True,
            stderr=True,
            remove=True
        )
        return container_output.decode("utf-8")
    except docker.errors.ContainerError as e:
        return e.stderr.decode("utf-8")
    except Exception as err:
        return f"[ERROR] Execution failed: {str(err)}"