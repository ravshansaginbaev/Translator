# Translator
Offline translator for over 100 languages

for  Windows:
python -m venv vevn
venv\Scripts\activate

For Ubuntu/Linux:
sudo apt-get install python3-tk

Libraries:
pip install torch
pip install transformers
pip install tkintertable   # (Tkinter itself comes preinstalled with Python, but on Linux you may need python3-tk)

GPU (CUDA) (optional): If you have an NVIDIA GPU, install PyTorch with CUDA support for much faster translation:
pip install torch --extra-index-url https://download.pytorch.org/whl/cu118
