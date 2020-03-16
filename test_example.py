import socket
import threading

import pytest

from tcp_server import TCPServer


@pytest.fixture(autouse=True)
def dummy_tcp_server():
    example_server = TCPServer()
    with example_server as tcp_server:
        thread = threading.Thread(target=example_server.listen_for_traffic)
        thread.daemon = True
        thread.start()
        yield example_server

'''
def test_example():
    HOST = '127.0.0.1'
    PORT = 9500

    data = ""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.settimeout(TIMEOUT_SOCKET)
        s.connect((IP_SERVER, PORT_SERVER))

        conn = s.makefile('wb')
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    assert data.decode() == "Received"

'''

import pyrealsense2 as rs
import numpy as np
import cv2

# # Configure depth and color streams
# pipeline = rs.pipeline()
# config = rs.config()
# config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
# pipeline.start(config)

# try:
#     while True:

#         # Wait for a coherent pair of frames: depth and color
#         frames = pipeline.wait_for_frames()
#         color_frame = frames.get_color_frame()
#         if not color_frame:
#             continue

#         # Convert images to numpy arrays
#         color_image = np.asanyarray(color_frame.get_data())

#         # Show images
#         cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
#         cv2.imshow('RealSense', color_image)
#         cv2.waitKey(1)
#         cv2.destroyAllWindows()

# finally:

#     # Stop streaming
#     pipeline.stop()


camera_type = "realsense"

def test_client():
    # client
    IP_SERVER = "127.0.0.1"
    PORT_SERVER = 9500
    TIMEOUT_SOCKET = 10
    DEVICE_NUMBER = 0

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_client.settimeout(TIMEOUT_SOCKET)
    socket_client.connect((IP_SERVER, PORT_SERVER))

    conn = socket_client.makefile('wb')

    try:
        
        byteImage = frame.tobytes()
        conn.write(byteImage)

        count += 1
        print('Frame: ', count, 'Size:', len(byteImage))

    except Exception as e:
        print("[Error] " + str(e))

    socket_client.close()
