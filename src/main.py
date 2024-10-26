from jinja2 import Environment, FileSystemLoader
import subprocess
import os

# Default values
DEFAULT_REGION = "us-west-2"
DEFAULT_PORT = 8388
DEFAULT_VPC_ID = "vpc-xxxxxxxx"
DEFAULT_SUBNET_ID = "subnet-xxxxxxxx"
DEFAULT_PASSWORD = "your_password"
DEFAULT_ENCRYPTION = "aes-gcm-256"

def get_user_input(prompt, default_value):
    user_input = input(f"{prompt} [{default_value}]: ")
    return user_input if user_input else default_value

def generate_tf_file(region, port, vpc_id, subnet_id, password, encryption):
    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template('main.tf.j2')

    # Render the template with user inputs or defaults
    main_tf_content = template.render(
        region=region,
        port=port,
        vpc_id=vpc_id,
        subnet_id=subnet_id,
        password=password,
        encryption=encryption
    )

    # Write the rendered content to main.tf
    with open('main.tf', 'w') as f:
        f.write(main_tf_content)

    print("Generated main.tf using template.")

def initialize_git():
    # Check if a .git directory already exists
    if not os.path.exists('.git'):
        subprocess.run(["git", "init"])
        print("Initialized a new Git repository.")
    else:
        print("Git repository already initialized.")

    # Create a .gitignore file if it doesn't exist
    if not os.path.exists('.gitignore'):
        with open('.gitignore', 'w') as gitignore:
            gitignore.write("*.tfstate\n*.tfstate.backup\n.terraform/\n")
        print("Created .gitignore for Terraform state files.")

def main():
    print("Welcome to the Shadowsocks ECS Deployment Generator!")

    # Get user inputs, falling back to defaults if no input is provided
    region = get_user_input("Enter AWS region", DEFAULT_REGION).lower()
    port = int(get_user_input("Enter port number", DEFAULT_PORT))
    vpc_id = get_user_input("Enter VPC ID", DEFAULT_VPC_ID).lower()
    subnet_id = get_user_input("Enter Subnet ID", DEFAULT_SUBNET_ID).lower()
    password = get_user_input("Enter Shadowsocks password", DEFAULT_PASSWORD)
    encryption = get_user_input(
        "Enter Shadowsocks encryption method:\n"
        " - ChaCha20-IETF-Poly1305 for mobile devices\n"
        " - XChaCha20-IETF-Poly1305 for enhanced security\n"
        " - AES-256-GCM for devices with hardware acceleration\n",
        DEFAULT_ENCRYPTION
    ).lower()

    # Generate the Terraform configuration file
    generate_tf_file(region, port, vpc_id, subnet_id, password, encryption)

    # Initialize Terraform
    subprocess.run(["terraform", "init"])

    # Automatically initialize Git and add Terraform state files
    initialize_git()

    # Add Terraform state files to Git
    subprocess.run(["git", "add", "*.tfstate*"])
    subprocess.run(["git", "commit", "-m", "Add Terraform state files"])
    print("Terraform state files added to Git.")

if __name__ == "__main__":
    main()