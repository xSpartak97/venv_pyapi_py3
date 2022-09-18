from setuptools import setup, find_packages


setup(name='ssqaapitest',
      version='1.0,',
      description='Practice API testing',
      author='Vlad Mura',
      author_email='murahovscky66@gmail,com',
      url='no url found',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
            "pytest==7.1.2",
            "pytest-html==3.1.1",
            "requests==2.28.0",
            "requests-oauthlib==1.3.1",
            "PyMySQL==1.0.2",
            "WooCommerce==3.0.0"
      ]
      )