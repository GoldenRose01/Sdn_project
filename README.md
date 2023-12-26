# TopologyDisplay - SDN - Backend
Softwarized And Virtualized mobile networks project 2022

## Authors
- Mattia Meneghin
- Francesco La Rosa
- Diamand Muka

## Dependencies
- Node (npm v10.1.0, nvm v0.39.5)
- Cors

## Environment
- Download the comnetsemu environment [here](https://www.granelli-lab.org/researches/relevant-projects/comnetsemu-labs)
- we used Virtualbox, so we set NAT with some port forwarding rules as follow:
    
    **Name** | **Protocol** | **Host IP** | **Host Port** | **Guest IP** | **Guest Port** 
    --- | --- | --- | --- |--- |--- 
    Back End | TCP | empty | 3000 | 10.0.2.15 | 3000
    Front End | TCP | empty | 8000 | 10.0.2.15 | 80
    API1 | TCP | empty | 8080 | 10.0.2.15 | 8080
    API2 | TCP | empty | 8082 | 10.0.2.15 | 8082
    SSH | TCP | empty | 2200 | 10.0.2.15 | 22

- Launch the Virtualbox Comnetsemu VM and then connect to the machine via ssh
    - ```ssh -p 2200 comnetsemu@localhost```
    - use the password: *comnetsemu*
- clone this repository inside
- ```npm install``` to install all the dependencies

- ```ryu-manager gui_start.py topologies/nome_filetopologia.py``` to start the gui part
- than you can run [the gui page](http://localhost:8080)
