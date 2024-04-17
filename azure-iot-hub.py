# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse


async def main():
    # The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
    conn_str = "HostName=testiothublezione.azure-devices.net;DeviceId=ur5;SharedAccessKey=iU6CHA6NXAtlh16bRYb6OEI7kYI8x8MZTAIoTL7/HOM="

    # The client object is used to interact with your Azure IoT hub.
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # connect the client.
    await device_client.connect()

    # Define behavior for handling methods
    async def method_request_handler(method_request):
        # Determine how to respond to the method request based on the method name
        if method_request.name == "shape1":
            payload = {"result": True, "data": "OK"}  # set response payload
            status = 200  # set return status code
            print("Perform shape 1")
        elif method_request.name == "shape2":
            payload = {"result": True, "data": "OK"}  # set response payload
            status = 200  # set return status code
            print("Perform shape 2")
        else:
            payload = {"result": True, "data": "OK"}  # set response payload
            status = 200  # set return status code
            print("Perform shape 3")

        # Send the response
        method_response = MethodResponse.create_from_method_request(method_request, status, payload)
        await device_client.send_method_response(method_response)

    # Set the method request handler on the client
    device_client.on_method_request_received = method_request_handler

    # Define behavior for halting the application
    def stdin_listener():
        while True:
            selection = input("Press Q to quit\n")
            if selection == "Q" or selection == "q":
                print("Quitting...")
                break

    # Run the stdin listener in the event loop
    loop = asyncio.get_running_loop()
    user_finished = loop.run_in_executor(None, stdin_listener)

    # Wait for user to indicate they are done listening for method calls
    await user_finished

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())