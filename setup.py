from setuptools import setup, find_packages

setup(
    name="gchat-card-builder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List dependencies here, for example:
        # 'requests',
    ],
    author="Pete Karl II",
    author_email="pete.karl@gmail.com",
    description="A clean, type-safe interface for generating rich chat responses to the Google Chat API using the CardsV2 schema.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pkarl/gchat-card-builder",  # Add your repo URL here
    classifiers=[
        "Development Status :: 3 - Alpha",  # or '5 - Production/Stable' if it's stable
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="google chat api, cardsv2, gchat, chatbot, chat bot, google chat",
)
