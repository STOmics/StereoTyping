from  setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='stereotyping',
    version='1.0.0',
    author='Huanghuaqiang',
    author_email='huanghuaqiang@genomics.cn',
    description=('Analysis workflow for ST with IF'),
    long_description=long_description,
    license='MIT License',
    keywords='Cell Typing via model based on ST with IF',
    url="https://github.com/STOmics/StereoTyping",

    packages=['stereotyping'], #需要打包的目录列表

    include_package_data=True,
    platforms='any',
    #需要安装的依赖包
    install_requires = [
        'anndata>=0.8.0',
        'scanpy>=1.9.1',
        'pandas>=1.4.3',
        'numpy>=1.22.3',
        'seaborn>=0.11.2',
        'matplotlib>=3.5.2',
        'scipy>=1.8.1',
        'opencv-python>=4.6.0.66',
        'xgboost>=1.7.5',
        'sklearn>=1.1.1',
        'shap>=0.38.1',
        'borutaShap>=1.0.16',
        'hyperopt>=0.2.7'
    ]
)