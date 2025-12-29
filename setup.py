"""Setup configuration for prediction-markets-api client library."""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="predictmarket",
    version="0.1.0",
    author="Anuj Jain",
    author_email="info@predictmarket.ai",
    description="Python client for accessing prediction markets data, factor returns, and thematic correlations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/predict-market/api-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.27.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
        ],
    },
    keywords="prediction markets api client kalshi polymarket finance quant trading analytics thematic correlations factor returns stock factor betas",
    project_urls={
        "Documentation": "https://github.com/predict-market/api-python/blob/main/README.md",
        "Source": "https://github.com/predict-market/api-python",
        "Bug Reports": "https://github.com/predict-market/api-python/issues",
    },
)
