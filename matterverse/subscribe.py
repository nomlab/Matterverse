import os
import re
from database import get_devices_from_database
from matter_xml_parser import parse_device_type_info, parse_clusters_info
from matter_utils import get_cluster_by_device_type, get_cluster_name_by_code
import json

async def subscribe_devices():
    devices = get_devices_from_database()
    for device in devices:
        node = device.get("NodeID")
        endpoint = device.get("Endpoint")
        device_type = device.get("DeviceType")
        device_type = f"0x{int(device_type):04X}"
        clusters = get_cluster_by_device_type(device_type)
        from matter_xml_parser import all_clusters
        for cluster in clusters:
            cluster_info = next((item for item in all_clusters if item.get("name") == cluster), None)
            if cluster_info:
                attributes = cluster_info.get("attributes", [])
                for attribute in attributes:
                    attribute_name = attribute.get("name")
                    if attribute_name != '':
                        attribute_name = re.sub(r'(?<!^)(?<![A-Z])(?=[A-Z])', '-', attribute_name).lower()
                        cluster_name = cluster.lower().replace("/", "")
                        command = f"{cluster_name} subscribe {attribute_name} 1 100 {node} {endpoint}"
                        from chip_tool_server import run_chip_tool_command
                        from chip_tool_server import response_queue
                        await run_chip_tool_command(command)
                        while True:
                            print(f"\033[1;34mCHIP\033[0m:     Waiting for response for NodeID: {node}, Endpoint: {endpoint}, Cluster: {cluster_name}, Attribute: {attribute_name}")
                            json_str = await response_queue.get()
                            json_data = json.loads(json_str)
                            node_id = json_data["ReportDataMessage"]["AttributeReportIBs"][0]["AttributeReportIB"]["AttributeDataIB"]["AttributePathIB"]["NodeID"]
                            endpoint_id = json_data["ReportDataMessage"]["AttributeReportIBs"][0]["AttributeReportIB"]["AttributeDataIB"]["AttributePathIB"]["Endpoint"]
                            cluster_code = json_data["ReportDataMessage"]["AttributeReportIBs"][0]["AttributeReportIB"]["AttributeDataIB"]["AttributePathIB"]["Cluster"]
                            attribute_code = json_data["ReportDataMessage"]["AttributeReportIBs"][0]["AttributeReportIB"]["AttributeDataIB"]["AttributePathIB"]["Attribute"]
                            cluster_code = f"0x{int(cluster_code):04X}"
                            attribute_code = f"0x{int(attribute_code):04X}"
                            if node == node_id and endpoint == endpoint_id and cluster_info.get("id") == cluster_code and attribute.get("code") == attribute_code:
                                print(f"\033[1;34mCHIP\033[0m:     Subscribe executed for NodeID: {node}, Endpoint: {endpoint}, Cluster: {cluster_name}, Attribute: {attribute_name}")
                                break