from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>TCP/IP Protocol Suite</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 60%;
                    margin: 20px auto;
                }
                th, td {
                    border: 1px solid #444;
                    padding: 10px;
                    text-align: center;
                }
                th {
                    background-color: #f2f2f2;
                }
                h2 {
                    text-align: center;
                    margin-top: 40px;
                }
            </style>
        </head>
        <body>
            <h2>TCP/IP Protocol Suite</h2>
            <table>
                <tr>
                    <th>Layer</th>
                    <th>Protocols</th>
                </tr>
                <tr>
                    <td>Application Layer</td>
                    <td>HTTP, HTTPS, FTP, SMTP, DNS, DHCP, Telnet, SNMP</td>
                </tr>
                <tr>
                    <td>Transport Layer</td>
                    <td>TCP, UDP</td>
                </tr>
                <tr>
                    <td>Internet Layer</td>
                    <td>IP, ICMP, ARP, IGMP</td>
                </tr>
                <tr>
                    <td>Network Access Layer</td>
                    <td>Ethernet, Wi-Fi, PPP</td>
                </tr>
            </table>
        </body>
        </html>
        '''
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()
