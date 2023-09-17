from setuptools import setup, find_packages

setup(
    name="gchatcardbuilder",
    version="0.1.1",
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
    url="https://github.com/pkarl/gchatcardbuilder",  # Add your repo URL here
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="google chat api, cardsv2, gchat, chatbot, chat bot, google chat",
)
