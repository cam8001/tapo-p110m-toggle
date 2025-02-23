from tapo import ApiClient
import os, sys
import asyncio

from typing import NoReturn

def handle_error(error: Exception) -> NoReturn:
    """Handle errors gracefully and exit."""
    print(f"Error during preflight check: {str(error)}", file=sys.stderr)
    sys.exit(1)

# see https://github.com/mihai-dinculescu/tapo/blob/main/tapo-py/examples/tapo_p110.py
async def main():
    try:
        await preflight_check()
    except Exception as e:
        handle_error(e)
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    ip_address = os.getenv("TAPO_P110M_IP_ADDRESS")
    
    client = ApiClient(tapo_username, tapo_password)
    device = await client.p110(ip_address)
    
    async def device_is_on() -> bool:
        device_info = await device.get_device_info()
        return device_info.device_on
    
    if (await device_is_on()):
        await device.off()
    else:
        await device.on()
        
def preflight_check():
    required_env_vars = ["TAPO_USERNAME", "TAPO_PASSWORD", "TAPO_P110M_IP_ADDRESS"]
    for env_var in required_env_vars:
        if env_var not in os.environ:
            raise Exception(f"Missing required environment variable: {env_var}")
        
# When run from poetry
def entry_point():
    asyncio.run(main())

# When run directly as a script
if __name__ == "__main__":
    asyncio.run(main())