# LizmotorsAssn
Using Python to search the internet for queries sent by the user (and Canoo Inc. as well)

## Setting up the project
### Prerequisites 
- Make sure python version 3.
- Ensure you have the latest version of Google Chrome installed.
- Install selenium by running the requirements.txt file.

  ```
   pip install requirements.txt
   ```
  <i>
  Starting from version 4.6.0 (November 4, 2022) selenium comes with Selenium Manager packed in distribution. Selenium Manager is a new tool that helps to get a 
  working environment to run Selenium out of the box. It: </i>
  
  - automatically discovers, downloads, and caches the drivers required by Selenium when these drivers are unavailable;
  - automatically discovers, downloads, and caches the browsers driven with Selenium (Chrome, Firefox, and Edge) when these browsers are not installed in the 
    local system.
  <br> (referenced from https://selenium-python.readthedocs.io/installation.html)
 ### Ruuning the web scraping script
 
 - Clone this github repository in your system by running
    ```
   git clone https://github.com/VinayakRaoDikshit/LizmotorsAssn.git
   ```
   
 - Use the python interpreter in your system to run the file gatherInfo.py
 - If it is your first time running this script, a file named Canoo.csv will automatically be created in the <b>parent directory</b> of this project. 
