Mission 7 — 


Task 7.1 —

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| LAN | Local Area Network covering a small geographical area like a single home, classroom, or office. | Home Wi-Fi connecting my Mac, phone, and smart TV. |
| MAN | Metropolitan Area Network spanning a larger physical area such as a university campus or an entire city. | A university campus network connecting multiple academic buildings and libraries. |
| WAN | Wide Area Network that spans broad regional, national, or global distances. | The global Internet connecting millions of private and public networks. |
| DNS | Domain Name System serves as the phonebook of the Internet, translating human-friendly domain names into computer IP addresses. | Translating example.com into 172.66.147.243 so machines know where to send requests. |
| Router | A networking hardware device that directs data packets between different networks based on IP addresses. | Home Wi-Fi router directing data packets between my laptop and my Internet Service Provider (ISP). |
| Protocol | A standardized set of rules and conventions that determine how data is formatted, transmitted, and received across a network. | HTTPS (HyperText Transfer Protocol Secure) for encrypted web traffic and TCP/IP for reliable packet transmission. |
| Packet switching | A communication method where digital data is broken into smaller chunks called packets, sent independently across available network routes, and reassembled at the destination. | Streaming a video or downloading a file where packets travel through different routers and arrive in order. |
| Client-server | A distributed architecture where client devices request services or resources, and centralized servers process and deliver responses. | Google Chrome (client) requesting a web page from a web server hosting the website. |

---

Task 7.2 —

Terminal activities performed:
1. Connectivity Test:
   ping -c 3 example.com
   Output observed:
   PING example.com (172.66.147.243): 56 data bytes
   64 bytes from 172.66.147.243: icmp_seq=0 ttl=59 time=30.417 ms
   64 bytes from 172.66.147.243: icmp_seq=1 ttl=59 time=30.553 ms
   64 bytes from 172.66.147.243: icmp_seq=2 ttl=59 time=25.472 ms
   3 packets transmitted, 3 packets received, 0.0% packet loss
   round-trip min/avg/max = 25.472/28.814/30.553 ms

2. DNS Lookup:
   nslookup example.com
   Output observed:
   Server: [redacted]
   Address: [redacted]
   Non-authoritative answer:
   Name: example.com
   Address: 172.66.147.243
   Address: 104.20.23.154

Questions answered:
- What a connectivity test helps you check:
  The ping test checks if a remote server is reachable over the network and measures latency (round-trip time in milliseconds). It also checks for packet loss to verify network stability.
- What information a DNS lookup displays:
  A DNS lookup displays the resolved IP addresses (IPv4 or IPv6) linked to a specific domain name, along with the DNS server that handled the query.
- Role of DNS when entering a website name:
  Humans remember domain names like example.com, but network routers only understand IP addresses. DNS automatically resolves the human name into the server's numeric IP address so the browser knows where to establish a connection.

---

Task 7.3 —

1. User enters URL: The user types a web address (such as https://example.com) into the web browser (the client) and presses Enter.
2. DNS Resolution: The browser checks its local cache; if not found, it queries a DNS resolver to convert the domain name example.com into its numeric IP address (172.66.147.243).
3. TCP and TLS Handshake: The client initiates a secure connection to the destination server using standard protocols (TCP 3-way handshake followed by a TLS/SSL cryptographic handshake for HTTPS).
4. Packet Transmission via Router: The client sends an HTTP GET request. The operating system breaks this request into packets, and local routers forward them across the Internet through the most efficient path.
5. Server Processing: The destination web server receives the packets, reassembles them, processes the request, and generates the requested resources (HTML, CSS, JavaScript).
6. Response and Rendering: The server sends the response packets back across the network to the client. The browser reassembles the packets, parses the HTML/CSS, and renders the interactive web page on the screen for the user.
