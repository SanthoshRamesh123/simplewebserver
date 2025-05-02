# EX01 Developing a Simple Webserver
## Date: 02.05.25

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content showing differences between TCP and IP in table form
content = """
<!DOCTYPE html>
<html>
<head>
    <title>Difference Between TCP and IP</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #eef2f3; padding: 20px; }
        h1 { color: #2c3e50; }
        table {
            width: 90%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
        }
        th, td {
            border: 1px solid #aaa;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #34495e;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Difference Between TCP and IP Protocols</h1>
    <table>
        <tr>
            <th>Feature</th>
            <th>TCP (Transmission Control Protocol)</th>
            <th>IP (Internet Protocol)</th>
        </tr>
        <tr>
            <td>Layer</td>
            <td>Transport Layer</td>
            <td>Internet Layer</td>
        </tr>
        <tr>
            <td>Connection Type</td>
            <td>Connection-Oriented</td>
            <td>Connectionless</td>
        </tr>
        <tr>
            <td>Reliability</td>
            <td>Reliable (ensures delivery, error-checking)</td>
            <td>Unreliable (no guarantee of delivery)</td>
        </tr>
        <tr>
            <td>Data Transmission</td>
            <td>Data sent in sequence as a stream</td>
            <td>Data sent as individual packets</td>
        </tr>
        <tr>
            <td>Error Handling</td>
            <td>Yes, with acknowledgment and retransmission</td>
            <td>Basic error checking only</td>
        </tr>
        <tr>
            <td>Speed</td>
            <td>Slower due to overhead</td>
            <td>Faster, minimal overhead</td>
        </tr>
        <tr>
            <td>Use Case</td>
            <td>Web, email, file transfer</td>
            <td>Routing data across networks</td>
        </tr>
    </table>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
print("Webserver is running at http://127.0.0.1:8000...")
httpd.serve_forever()
```
## OUTPUT:
![alt text](<Screenshot 2025-05-02 182412-1.png>)
![alt text](<Screenshot 2025-05-02 182425.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
