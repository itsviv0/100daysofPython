## Day 48: Selenium Webdriver browser and Game playing bot

- install and setup selenium
  - goto chromo browser and check the version, copy the full version
  - paste this link in the browser to download the chromedriver:
      ``` https://storage.googleapis.com/chrome-for-testing-public/<chrome-version>/linux64/chromedriver-linux64.zip```
  - extract the zip file
  - move the chromedriver file to ```/usr/bin/``` folder
      ```sh
      sudo mv chromedriver /usr/bin/chromedriver
      sudo chown root:root /usr/bin/chromedriver
      sudo chmod +x /usr/bin/chromedriver
      ```
  - test the chromedriver
      ```sh
      chromedriver --url-base=/wd/hub
      ```
- finding and selecting elements on browser with selenium
- automate filling forms and clicking buttons on the webpage

![image](https://github.com/user-attachments/assets/aeb877dd-a77c-465a-8ee5-d22939153bf1)
