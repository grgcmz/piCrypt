import logging
import os
import subprocess

logger = logging.getLogger('usb')
usb_device = '/dev/sda1'  # Update this with the correct device name
usb_mount_point = '/mnt/usb'

# Check if the USB mount point exists
if not os.path.exists(usb_mount_point):
    os.makedirs(usb_mount_point)

# Check if the USB stick is already mounted
mounted = subprocess.run(['grep', '-qs', usb_mount_point, '/proc/mounts'], stdout=subprocess.PIPE).returncode == 0

if not mounted:
    # Mount the USB stick
    mount_result = subprocess.run(['sudo', 'mount', usb_device, usb_mount_point], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if mount_result.returncode == 0:
        logger.info("USB Stick mounted successfully.")
    else:
        logger.error(f"Failed to mount USB Stick.\n{mount_result.stderr.decode('utf-8')}")
        # print(mount_result.stderr.decode('utf-8'))
else:
    logger.info("USB Stick is already mounted.")

# List the contents of the USB stick
usb_contents = os.listdir(usb_mount_point)

# Print the contents
logger.info("Contents of USB Stick:")
for item in usb_contents:
    logger.info(item)
