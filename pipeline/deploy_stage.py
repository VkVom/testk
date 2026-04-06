"""
===============================================================
   STAGE 4: DEPLOY STAGE (Simulated)
===============================================================

WHAT IS THE DEPLOY STAGE?
  Simulates pushing the code to a live server.
  In real projects this would upload to AWS/Azure.
  Here it prints the steps and saves a deployment log.

  Returns the build number so the HTML report can show it.
"""

import datetime
import os
import time
import random


def run_deploy():
    """
    Simulates deployment and returns the build number string.
    """

    # Generate a unique build number
    date_part = datetime.datetime.now().strftime("%Y%m%d")
    build_number = f"BUILD-{date_part}-{random.randint(1000, 9999)}"
    deploy_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("  Target Environment : STAGING")
    print(f"  Build Number       : {build_number}")
    print(f"  Application        : EdTech Learning Platform v1.0.0")
    print()

    # Simulate deployment steps with small delays
    steps = [
        "Connecting to deployment server...",
        "Packaging application files...",
        "Uploading code to server...",
        "Stopping old version of application...",
        "Installing new version...",
        "Running database migrations...",
        "Starting new version of application...",
        "Running health check...",
        "Deployment verification complete!",
    ]

    for step in steps:
        print(f"  [DEPLOY] {step}")
        time.sleep(0.3)

    # Save deployment log
    os.makedirs("reports", exist_ok=True)
    with open("reports/deployment_log.txt", 'w') as f:
        f.write("DEPLOYMENT LOG\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Build Number  : {build_number}\n")
        f.write(f"Environment   : STAGING\n")
        f.write(f"Deploy Time   : {deploy_time}\n")
        f.write(f"Application   : EdTech Learning Platform\n")
        f.write(f"Version       : v1.0.0\n")
        f.write(f"Deployed By   : CI/CD Pipeline (Automated)\n")
        f.write(f"Target Server : edtech-staging.example.com\n\n")
        f.write("Steps Executed:\n")
        for i, step in enumerate(steps, 1):
            f.write(f"  Step {i}: {step}\n")
        f.write("\nSTATUS: DEPLOYMENT SUCCESSFUL (Simulated)\n")

    print(f"\n  [INFO] Deployment log saved to: reports/deployment_log.txt")

    return build_number
