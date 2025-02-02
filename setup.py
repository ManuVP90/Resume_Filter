from setuptools import setup, find_packages

setup(
    name="job_experience_evaluator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        'console_scripts': [
            'evaluate-job-experience=src.main:main',
        ],
    },
)
