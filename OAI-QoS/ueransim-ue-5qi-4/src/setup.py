from setuptools import find_packages, setup

package_name = 'nodes_4dock'

setup(
    name=package_name,
    version='0.0.1',
    packages=['nodes_4dock'],
    py_modules=[
        'nodes_4dock.node_publisher_1',
        'nodes_4dock.node_subscriber_1',
        'nodes_4dock.node_publisher_2',
        'nodes_4dock.node_subscriber_2',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='RB',
    author_email='your_email@example.com',
    maintainer='RB',
    maintainer_email='your_email@example.com',
    description='My ROS 2 package with two publishers and two subscribers',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_publisher_1 = nodes_4dock.node_publisher_1:main',
            'node_subscriber_1 = nodes_4dock.node_subscriber_1:main',
            'node_publisher_2 = nodes_4dock.node_publisher_2:main',
            'node_subscriber_2 = nodes_4dock.node_subscriber_2:main',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/nodes_4dock']),
        ('share/nodes_4dock', ['package.xml']),
    ],
)
