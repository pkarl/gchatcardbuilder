from setuptools import setup, find_packages

setup(
    name='cardsv2-builder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List dependencies here, for example:
        # 'requests',
    ],
    author='Pete Karl II',
    author_email='pete.karl@gmail.com',
    description='A clean, type-safe interface for generating chat responses to the Google Chat API using the CardsV2 schema.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/petekarl/cardsv2-builder',  # Add your repo URL here
    classifiers=[
        'Development Status :: 3 - Alpha',  # or '5 - Production/Stable' if it's stable
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',  # Change the license if you have a different one
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='google chat api, cardsv2, builder pattern, interface',
)
