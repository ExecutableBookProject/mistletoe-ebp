from importlib import import_module

from setuptools import find_packages, setup


setup(
    name="mistletoe-ebp",
    version=import_module("mistletoe").__version__,
    description="A fast, extensible Markdown parser in pure Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ExecutableBookProject/mistletoe-ebp",
    project_urls={"Documentation": "https://mistletoe-ebp.readthedocs.io"},
    author="Chris Sewell",
    author_email="chrisj_sewell@hotmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mistletoe = mistletoe.cli.parse:main",
            "mistletoe-bench = mistletoe.cli.benchmark:main",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup",
    ],
    keywords="markdown lexer parser development",
    python_requires="~=3.6",
    install_requires=["attrs~=19.3"],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black==19.10b0", "pre-commit==1.17.0"],
        "testing": ["coverage", "pytest>=3.6,<4", "pytest-cov", "pytest-regressions"],
        "rtd": ["sphinx>=2,<3", "myst-parser~=0.6.0a3", "pyyaml"],
        "benchmark": [
            "commonmark~=0.9.1",
            "markdown~=3.2",
            "mistune~=0.8.4",
            "panflute~=1.12",
        ],
    },
    zip_safe=False,
)
