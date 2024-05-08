#/bin/bash
CNAME="httpd"
CID=$(sudo docker inspect $CNAME -f '{{.State.Pid}}')
sudo mkdir -p /var/run/netns
# link network namespace for `some_container`
sudo ln -sfT /proc/$CID/ns/net /var/run/netns/$CNAME
# view the interface of the container
sudo ip netns exec $CNAME ip -br -c link
IFACE=$(sudo ip netns exec $CNAME ip -br -c link| grep "eth0"| awk -F" " '{print $1}')
echo "Iface: $IFACE"
# add traffic control policy to the interface in network namespace `some_container`
# tc -n some_container qdisc add dev eth0 tbf rate 1024kbps 1024b limit 1024b
# update tc 2023/05/19
sudo tc -n $CNAME qdisc add dev eth0 handle 10: root tbf limit 1024 burst 2048 rate 1024