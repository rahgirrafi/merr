from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'merr_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #include launch files
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='host',
    maintainer_email='host@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test_node = merr_robot.test_node:main',
            'camera = merr_robot.camera:main',
            'minimal_subscriber = merr_robot.minimal_subscriber:main',
        ],
    },
)
