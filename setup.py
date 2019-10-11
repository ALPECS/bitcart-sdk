import os

from setuptools import find_packages, setup

from sync_generator import main as generate

SYNC_REQS = ["jsonrpcclient[requests]"]
ASYNC_REQS = ["jsonrpcclient[aiohttp]"]


def main() -> None:
    SYNC = os.getenv("SYNC", False)
    if SYNC:
        generate()

    setup(
        name="bitcart" if SYNC else "bitcart-async",
        packages=find_packages(),
        version="0.7.0",
        license="MIT",
        description="Bitcart coins support library",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        author="MrNaif2018",
        author_email="chuff184@gmail.com",
        url="https://github.com/MrNaif2018/bitcart-sdk",
        keywords=["electrum", " daemon", "bitcart"],
        install_requires=SYNC_REQS if SYNC else ASYNC_REQS,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Build Tools",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
    )


if __name__ == "__main__":
    main()
