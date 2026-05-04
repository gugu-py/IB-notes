other keys:
- cookies

# Different types of networks – Topic 3 Networks


## What is a network?

* ==A network, in the context of computer science, is a collection of interconnected devices (computers, smartphones, servers, printers) that can communicate and share resources with each other==
* Networks facilitate the exchange of data, information and services.  They enable collaboration and communication between people and systems.


## Objective

* **Objective 3.1.1:** To be able to identify different types of networks.

## Local Area Network (LAN)

* A **Local Area Network (LAN)** is a computer network that connects computers over a limited area such as a home, school, business or factory【412466278376878†screenshot】.
 
* The next slide labels the devices in the same diagram: **laptop**, **router**, **switch**, **printer**, **desktop** computers, **LAN cables** and **Internet**.

==devices to setup LAN==:
(Wireless) router;  
A central hub for all the computers to connect to;  
Enables wireless network packet forwarding and routing;

Wireless Network Interface Card (NIC);  
To allow the computer to ‘talk to’ the (wireless) router;

Wireless access points;  
allow Wi-Fi devices to connect to a wired network;

Wireless repeaters;  
To expand the reach of the network;

## Virtual Local Area Network (VLAN)

* A **VLAN** creates separate logical networks on a single physical infrastructure.  The slide explains that you can think of it as virtualising an office building with different departments on different floors without needing separate physical networks.  A diagram of an office tower accompanies the text.
* Another slide lists the benefits of VLANs:
  * **Security:** Sensitive data and devices can be isolated on their own virtual network
  * **Efficiency:** Traffic is separated, reducing congestion
  * **Management:** Simplifies network administration
  * **Flexibility:** Devices can be moved between logical networks without rewiring【299157451200821†screenshot】.

## Wide Area Network (WAN)

* A **Wide Area Network (WAN)** is a network of devices spread over a large geographical area.  WANs rely on telecommunications networks; the Internet is the most well‑known example of a WAN

## Storage Area Network (SAN)

* A **Storage Area Network (SAN)** is a specialised, high‑speed network dedicated to connecting servers and storage devices【391736713833902†screenshot】.  It acts like a private highway for moving data between servers and storage resources.
* **How is a SAN used?** The slide lists several uses of SANs:
  * **Centralised storage:** SANs allow multiple servers to access a shared pool of storage devices (such as disk arrays or tape libraries) as if the drives were locally attached.  This simplifies storage management and improves resource utilisation【17127347711306†screenshot】.
  * **High performance:** SANs use high‑speed protocols and dedicated hardware (e.g., fibre‑optic cables and SAN switches) to achieve fast, reliable data transfers.  They are critical for applications demanding high I/O performance【17127347711306†screenshot】.
  * **Scalability:** SANs can be easily expanded by adding more storage devices or servers to accommodate growing data requirements【17127347711306†screenshot】.
  * **Data protection:** SANs often include features such as data replication, backup and disaster‑recovery mechanisms to ensure data availability and integrity【17127347711306†screenshot】.

## Wireless Local Area Network (WLAN)

* A **Wireless Local Area Network (WLAN)** is a computer network that connects computers over a limited area (such as a home, school, business or factory) using wireless technologies【23879310981244†screenshot】.

## LAN and WLAN together

* A slide explains that modern LANs often incorporate WLAN capabilities.  This combination allows for greater flexibility and mobility for users with laptops, smartphones and other wireless devices.  Many homes and businesses use both wired and wireless connections; the wired LAN provides stability and speed, while the WLAN (using radio waves) provides mobility.

## The Internet

* The Internet is described as a vast global network of interconnected computer networks enabling communication and data exchange.  It is essentially a **“network of networks”** that spans the globe, connecting countless computers, servers and other devices【717697814860347†screenshot】.
* A slide summarises the main services and applications built on top of the Internet【717697814860347†screenshot】:
  * **World Wide Web (WWW):** A collection of interconnected documents and resources accessed through web browsers.
  * **Email:** Electronic messaging for sending and receiving messages.
  * **Social media:** Platforms for online interaction and communication.
  * **File sharing:** Transferring files between computers.
  * **Streaming:** Real‑time audio and video delivery over the network.
  * **…and many more.**

## Intranet

* **Definition:** An intranet is a private network accessible only to authorised users within an organisation (e.g., employees)
* **Purpose:** Facilitates internal communication, collaboration and access to company resources
* **Examples of use:**
  * Sharing company news, policies and documents
  * Providing access to internal tools and applications (such as HR systems or project‑management tools)
  * Facilitating employee communication and collaboration via forums, chat or wikis
* **Security:** Intranets are typically protected by **firewalls** and other security measures to prevent unauthorised access from outside the organisation



## Extranet

* **Definition:** An extranet is a controlled private network that extends an organisation’s intranet to authorised external users (e.g., partners, suppliers or customers)【854731286110774†screenshot】.
* **Purpose:** Facilitates secure collaboration and information sharing with external parties
* **Examples of use:**
  * Providing partners or suppliers access to order‑tracking or inventory systems
  * Enabling customers to check their account status or support tickets
  * Sharing project information with external collaborators
* **Security:** Employs security measures similar to those used by intranets but with controlled access points for specific external users

### Key differences between intranet and extranet

| Feature           | Intranet                                 | Extranet                                      |
| ----------------- | ---------------------------------------- | --------------------------------------------- |
| **Accessibility** | Internal users only                      | Internal users + authorised external users    |
| **Purpose**       | Internal communication and collaboration | Secure collaboration with external parties    |
| **Security**      | High security and restricted access      | Controlled access for specific external users |

## Virtual private network (VPN)

* A **Virtual Private Network (VPN)** creates a secure, encrypted connection over a public network such as the Internet.  It allows users to send and receive data as if they were directly connected to a private network, preserving privacy and security.

## Personal Area Network (PAN)

* A **Personal Area Network (PAN)** is a network of devices over a limited range.  The slide explains that an example is the Bluetooth connection between a mobile phone and wireless headphones

## Peer‑to‑peer (P2P) network

* A **Peer‑to‑Peer (P2P) network** is a network of computers that share resources and are connected to each other without a central server【508934956798726†screenshot】.


## Common network devices

* **Network interface card:** A network interface controller (NIC), also known as a network interface card or LAN adapter, is a computer hardware component that connects a computer to a computer network.
* **Hub:** A hub is a device for connecting multiple devices together.  It has multiple ports and any input signal at a port is sent out of every other port except the original port【228110217963192†screenshot】.
* **Switch:** A network switch connects devices together on a computer network.  Unlike a hub, a switch sends data only to the device that needs to receive it rather than out of every connected port.
* **Router:** A router connects two or more networks together.  A common use is to connect a LAN such as a home network to a WAN such as the Internet via an Internet Service Provider (ISP)

## What is globalisation?

* Globalisation is a term used to describe the increasing connectedness and interdependence of world cultures and economies
* Globalisation is also the process by which businesses or other organisations develop international influence or start operating on an international scale

---

# Security

hardware security: locked doors, CCTV, surveilence, 

firewall: a software that controls inbound/outbound network traffic from a system with pre-defined rule

# Other concepts

VPN ==definition==: VPN is built by creating a virtual point-to-point connection using dedicated connections, technologies of traffic encryption, and virtual tunneling protocols.
- technologies: VPN client software, SSL

Standards: agreements to enhance interoperability and compatibility

Protocols: Set of rules for data transmission
- advantages: data integrity, prevent deadlock, error checking

Packet switching:
1. a file is broken into data packets
2. packets are sent independently (take different paths)
3. packets are reassembled and checked for error

encryption: Data encryption refers to calculations/algorithms that transform plain text into a form that is non-readable to unauthorized parties

OSI layers:
1. Application layer: internet service directly to application (http/https)
2. Presentation layer: data format (JPG, Json, etc.)
3. Session Layer: manages sessions
4. transport layer: responsible for data transmission reliability (udp/tcp)
5. Network layer: routing between networks with IP (packets)
6. data link layer: communication in LAN (frame)
7. physical layer: communication between physical devices (bits)

speed of data transmission (phone):
1. network technology (3G, 4G)
2. distance to cell tower
3. user number in the area
4. feature of device/phone

