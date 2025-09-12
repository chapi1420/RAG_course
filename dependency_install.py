import subprocess
import sys

packages = [
    "ibm-watsonx-ai==0.2.6",
    "langchain==0.1.16",
    "langchain-ibm==0.1.4",
    "transformers==4.41.2",
    "huggingface-hub==0.23.4",
    "sentence-transformers==2.5.1",
    "chromadb",
    "wget==3.2",
    "torch --upgrade --index-url https://download.pytorch.org/whl/cpu"
]

for pkg in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + pkg.split())
print("All packages installed successfully.")