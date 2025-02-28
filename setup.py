import setup

setup(
    name='draw_heap',
    version='1.0.0',
    py_modules=['draw_heap'],
    entry_points={
        'console_scripts': [
            'draw_heap=draw_heap:main',
        ],
    },
    install_requires=[
        'Flask'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to draw a binary heap as a binary tree and display it on a web page.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
