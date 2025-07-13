# node_publisher_1.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode1(Node):
    def __init__(self):
        super().__init__('publisher_node_1')
        self.publisher = self.create_publisher(String, 'first_topic', 10)
        self.count1 = 0
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1s timer

    def timer_callback(self):
        msg = String()
        msg.data = f"first topic msg {self.count1}"
        self.publisher.publish(msg)
        #self.get_logger().info(f"Publishing: {msg.data}")
        self.count1 += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
