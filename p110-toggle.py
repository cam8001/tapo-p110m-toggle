from tapo import ApiClient
import os
import asyncio

# see https://github.com/mihai-dinculescu/tapo/blob/main/tapo-py/examples/tapo_p110.py
async def main():
    tapo_username = os.getenv("TAPO_USERNAME")
    tapo_password = os.getenv("TAPO_PASSWORD")
    ip_address = os.getenv("TAPO_FAN_IP_ADDRESS")
    
    client = ApiClient(tapo_username, tapo_password)
    device = await client.p110(ip_address)
    
    async def device_is_on() -> bool:
        device_info = await device.get_device_info()
        return device_info.device_on
    
    if (await device_is_on()):
        await device.off()
    else:
        await device.on()

if __name__ == "__main__":
    asyncio.run(main())