*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}      localhost:5001
${DELAY}       0.1 seconds
${HOME_URL}    http://${SERVER}
${RESET_URL}   http://${SERVER}/reset_db
${CREATE_URL}  http://${SERVER}/new_reference
${BROWSER}     chrome
${HEADLESS}    false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Books
    Go To  ${RESET_URL}

Go To Starting Page
    Go To  ${HOME_URL}

Go To New Reference Page
    Go To  ${CREATE_URL}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Number
    [Arguments]  ${number}
    Input Text  number  ${number}

Set Series
    [Arguments]  ${series}
    Input Text  series  ${series}

Set Address
    [Arguments]  ${address}
    Input Text  address  ${address}

Set Edition
    [Arguments]  ${edition}
    Input Text  edition  ${edition}

Set Month
    [Arguments]  ${month}
    Input Text  month  ${month}

Set Note
    [Arguments]  ${note}
    Input Text  note  ${note}

Set Annote
    [Arguments]  ${annote}
    Input Text  annote  ${annote}

Set Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Set Organization
    [Arguments]  ${organization}
    Input Text  organization  ${organization}

