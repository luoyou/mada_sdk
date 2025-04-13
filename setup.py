import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="mada sdk",
    version="1.0",
    author="luoyou",
    author_email="luoyou1014@163.com",
    description="mada process sdk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luoyou/mada_sdk",
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        "redis",
    ],
    python_requires=">=3",
)
