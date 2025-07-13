# node_publisher_2.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode2(Node):
    def __init__(self):
        super().__init__('publisher_node_2')
        self.publisher = self.create_publisher(String, 'second_topic', 10)
        self.count2 = 0
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1s timer

    def timer_callback(self):
        msg = String()
        msg.data = f"second topic msg {self.count2}"
        self.publisher.publish(msg)
        #self.get_logger().info(f"Publishing: {msg.data}")
        self.count2 += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
