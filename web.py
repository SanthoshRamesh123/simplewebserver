from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML content with TCP/IP protocols in a table
content = """
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }
        h1 { color: #333; }
        table {
            width: 60%;
            border-collapse: collapse;
            margin-top: 20px;
            background-color: #fff;
        }
        th, td {
            border: 1px solid #999;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <table>
        <tr>
            <th>Layer</th>
            <th>Protocols</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, FTP, SMTP, DNS, Telnet</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>IP, ICMP, IGMP</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, ARP, PPP</td>
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
print("My webserver is running on http://127.0.0.1:8000...")
httpd.serve_forever()
