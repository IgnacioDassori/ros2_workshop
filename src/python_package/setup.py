from setuptools import find_packages, setup

package_name = 'python_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, [
            'launch/conversation_launch.py',
            'launch/turtlebot_launch.py'
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='idassori',
    maintainer_email='ignacio.dassori.w@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = python_package.talker:main',
            'listener = python_package.listener:main',
            'service = python_package.service:main',
            'client = python_package.client:main' 
        ],
    },
)
