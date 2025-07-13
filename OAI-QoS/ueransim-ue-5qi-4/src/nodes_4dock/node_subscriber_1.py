# node_subscriber_1.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode1(Node):
    def __init__(self):
        super().__init__('subscriber_node_1')
        self.subscription = self.create_subscription(
            String,
            'first_topic',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode1()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
