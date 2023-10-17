from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customer_dashboard/__init__.py
from customer_dashboard import __version__ as version

setup(
	name="customer_dashboard",
	version=version,
	description="A customized dashboard for erpnext",
	author="inbox logistics",
	author_email="abrar@inbox.com.qa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
