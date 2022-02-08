## HAEMOSU (Human Animal Enhanced Microbiome Open Source Utility)
![HAMOSU_LOGO_WHITE22](https://user-images.githubusercontent.com/97942052/153062244-1533ca18-9430-4d0f-8baa-a6419c19ec86.png)

**Welcome to HAEMOSU!!**

**랩미팅용 임시 리드미 작업**

HAEMOSU-gui can be install through `pip`, `conda`.
```
pip install -i https://test.pypi.org/simple/ haemosu-gui
or
conda install --use-local haemosu
```
You can also install HAEMOSU-gui manually.

HAEMOSU-gui requres `PyQt6`, which can be installed through `pip`, `conda`.
Please type the following codes in command line

```
cd path_to_your_folder/
git clone https://github.com/HanJune-Kim/haemosu_test.git
pip install PyQt6 PyQt6-WebEngine pyqtdarktheme psutil pandas 
```

Append `HAEMOSU PATH` to the `~/.bashrc`
```
export PATH=/path_to_haemosu-gui/:$PATH
export PATH=/path_to_haemosu-gui/haemosu-command:$PATH
source ~/.bashrc
```
