# Example usage:
HOST = "192.168.0.1"  # Replace with SSH host, IP address, or hostname
PORT = 22023            # Extron SSH PORT
USERNAME = "admin"
PASSWORD = "ABCDEF"   # Replace with password
URI = "udp://@238.XXX.XXX.XXX:1234"  # Replace with URI




import time
import paramiko

def ssh_setup(host, port, username, password, URI):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to client via ssh
        ssh.connect(host, port=port, username=username, password=password, timeout=5)

    # Error Handling
    except paramiko.AuthenticationException:
        print(f"Failed to connect to {host}:{port} with the provided credentials.")
        return
    except paramiko.SSHException as e:
        print(f"An SSH error occurred: {str(e)}")
        return
    except Exception as e:
        print(f"Failed to connect to {host}:{port}: {str(e)}")
        return


    # Invoke an interactive shell
    ssh_shell = ssh.invoke_shell()

    # Wait
    time.sleep(.5)

    # Print IP Address
    ssh_shell.send("\x1bCI\x0d")

    # Set Volume Level:
    ssh_shell.send("-4V\x0d")

    # 1: Load URI Playlist...
    command = "\x1bU1*" + URI + "PLYR\x0d"
    ssh_shell.send(command)

    # 3: Play Playlist...
    ssh_shell.send("\x1bS1*1PLYR\x0d")

    while True:
        if ssh_shell.recv_ready():
            output = ssh_shell.recv(1024).decode('utf-8')
            print(output, end='')
        else:
            time.sleep(0.05)
            if ssh_shell.recv_ready():
                output = ssh_shell.recv(1024).decode('utf-8')
                print(output, end='')
            else:
               break

    # Wait for a bit to allow the command to execute and receive output
    time.sleep(.5)

    ssh.close()



# SSH into the host, send commands, and output everything to the console
ssh_setup(HOST, PORT, USERNAME, PASSWORD, URI)



